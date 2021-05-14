from flask import Flask, flash, render_template, request, redirect, url_for
from Forms import CreateConsultForm, SearchVisits, PtVisit, Payment
import shelve, JHClass, addVisit
import hashlib

def encrypt_data(hash_string):
    sha_signature = \
        hashlib.sha256(hash_string.encode()).hexdigest()
    return sha_signature

def is_later_date(start, search):
    search = search.strftime("%d %m %Y")
    start = start[-2:] + "-" + start[5:7] + "-" + start[:4]
    if int(search[-4:]) < int(start[-4:]):
        return False
    elif int(search[-4:]) > int(start[-4:]):
        return True
    else:
        if int(search[3:5]) < int(start[3:5]):
            return False
        elif int(search[3:5]) > int(start[3:5]):
            return True
        else:
            if int(search[:2]) < int(start[:2]):
                return False
            else:
                return True

def is_earlier_date(end, search):
    search = search.strftime("%d %m %Y")
    end = end[-2:] + "-" + end[5:7] + "-" + end[:4]
    if int(search[-4:]) < int(end[-4:]):
        return True
    elif int(search[-4:]) > int(end[-4:]):
        return False
    else:
        if int(search[3:5]) < int(end[3:5]):
            return True
        elif int(search[3:5]) > int(end[3:5]):
            return False
        else:
            if int(search[:2]) <= int(end[:2]):
                return True
            else:
                return False

app = Flask(__name__)
addedThePt = 0
displayedThePt = 0
visit = ''

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/createConsultation', methods=['GET','POST'])
def create_consultation():
    create_form = CreateConsultForm(request.form)
    clinicsList = {}
    db = shelve.open('storage.db', 'r')
    try:
        clinicsList = db['ClinicList']
    except:
        print("Error loading database file")
    db.close()

    if request.method == 'POST':
        bookings_dict = {}
        db = shelve.open('storage.db', 'c')
        try:
            bookings_dict = db['Bookings']
        except:
            print("Error in retrieving Bookings from storage.db.")

        booking = JHClass.OnlineConsultation(create_form.fullname.data, create_form.location.data, create_form.clinic.data, create_form.symptoms.data, create_form.notes.data, create_form.timing.data, create_form.nric.data, create_form.date.data)
        bookings_dict[booking.get_nric()] = booking
        print(bookings_dict)
        db['Bookings'] = bookings_dict

        db.close()

        return redirect(url_for('home'))
    return render_template('createConsultation.html', form=create_form, clinicsList=clinicsList)

@app.route('/searchPtVisits', methods=['GET', 'POST'])
def search_pt():
    search = SearchVisits(request.form)
    if request.method == 'POST':
        searched = search.data
        db = shelve.open('storage.db', 'c')
        pat_vis = {}
        print(searched)
        try:
            pat_vis = db['ptVisits']
        except:
            print("Error retrieving data")
        db.close()
        dict = {}

        if searched['fromDate'] == '' and searched['toDate'] == '' and searched['searchBy'] == 'Name' and searched['searchFor'] == '':
            pass

        else:
            for i in pat_vis:
                #need identifier for clinic name
                if searched['searchFor'] == '' and searched['fromDate'] != '' and searched['toDate'] != '':
                    if is_earlier_date(searched['toDate'], pat_vis[i].get_keep_date()) and is_later_date(searched['fromDate'], pat_vis[i].get_keep_date()):
                        dict[i] = pat_vis[i]
                elif searched['searchFor'] == '' and searched['fromDate'] != '':
                    if is_later_date(searched['fromDate'], pat_vis[i].get_keep_date()):
                        dict[i] = pat_vis[i]

                elif searched['searchFor'] != '' and searched['fromDate'] != '' and searched['toDate'] != '':
                    if is_earlier_date(searched['toDate'], pat_vis[i].get_keep_date()) and is_later_date(searched['fromDate'], pat_vis[i].get_keep_date()):
                        if searched['searchBy'] == 'visitno' and searched['searchFor'].lower() == pat_vis[i].get_visit_num().lower():
                            dict[i] = pat_vis[i]
                        elif searched['searchBy'] == 'NRIC' and searched['searchFor'].lower() == pat_vis[i].get_nric().lower():
                            dict[i] = pat_vis[i]
                        elif searched['searchBy'] == 'Name' and searched['searchFor'].lower() in pat_vis[i].get_fullname().lower():
                            dict[i] = pat_vis[i]

                elif searched['searchFor'] != '' and searched['fromDate'] != '':
                    if is_later_date(searched['fromDate'], pat_vis[i].get_keep_date()):
                        if searched['searchBy'] == 'visitno' and searched['searchFor'].lower() == pat_vis[i].get_visit_num().lower():
                            dict[i] = pat_vis[i]
                        elif searched['searchBy'] == 'NRIC' and searched['searchFor'].lower() == pat_vis[i].get_nric().lower():
                            dict[i] = pat_vis[i]
                        elif searched['searchBy'] == 'Name' and searched['searchFor'].lower() in pat_vis[i].get_fullname().lower():
                            dict[i] = pat_vis[i]

                else:
                    if searched['searchBy'] == 'visitno' and searched['searchFor'].lower() == pat_vis[i].get_visit_num().lower():
                        dict[i] = pat_vis[i]
                    elif searched['searchBy'] == 'NRIC' and searched['searchFor'].lower() == pat_vis[i].get_nric().lower():
                        dict[i] = pat_vis[i]
                    elif searched['searchBy'] == 'Name' and searched['searchFor'].lower() in pat_vis[i].get_fullname().lower():
                        dict[i] = pat_vis[i]
        search.fromDate.data = ''
        search.toDate.data = ''

        return render_template('results.html', pt_visits=dict, form=search)
    global addedThePt
    global displayedThePt
    if displayedThePt < addedThePt:
        global visit
        displayedThePt += 1
        return render_template('searchPtVisits.html', form=search, added=1, pt=visit.get_fullname(), visit=visit)
    return render_template('searchPtVisits.html',  form=search)

@app.route('/updateVisit/<string:sig>', methods=['GET', 'POST'])
def update_visit(sig):
    update_pt_visit = PtVisit(request.form)
    if request.method == 'POST':
        pt_visits = {}
        db = shelve.open('storage.db', 'w')
        pt_visits = db['ptVisits']

        keepDate = update_pt_visit.visitDate.data
        visit_date = (update_pt_visit.visitDate.data.strftime("%d %m %Y").replace(' ', '-'))
        drugNameList = update_pt_visit.drugNameList.data
        drugPriceList = update_pt_visit.drugPriceList.data
        drugQtyList = update_pt_visit.drugQtyList.data
        drugAmtList = update_pt_visit.drugAmtList.data

        for i in range(len(drugNameList)):
            if drugNameList[i] == '':
                drugNameList.pop(i)

        print(update_pt_visit.drugNameList.data)
        print(update_pt_visit.drugPriceList.data)
        pt = pt_visits.get(sig)
        pt.set_fullname(update_pt_visit.ptName.data)
        pt.set_nric(update_pt_visit.nric.data)
        pt.set_visit_date(visit_date)
        pt.set_charge_type(update_pt_visit.chargeType.data)
        pt.set_allergies(update_pt_visit.allergies.data)
        pt.set_company(update_pt_visit.company.data)
        pt.set_mc_day(update_pt_visit.mcDay.data)
        pt.set_mc_reason(update_pt_visit.mcReason.data)
        pt.set_mc_date(update_pt_visit.mcDate.data)
        pt.set_pri_diagnosis(update_pt_visit.priDiagnosis.data)
        pt.set_sec_diagnosis(update_pt_visit.secDiagnosis.data)
        pt.set_drug_list(drugNameList)
        pt.set_drug_price_list(drugPriceList)
        pt.set_drug_qty_list(drugQtyList)
        pt.set_drug_amt_list(drugAmtList)
        pt.set_drug_name(update_pt_visit.drugName.data)
        pt.set_drug_price(update_pt_visit.drugPrice.data)
        pt.set_drug_amt(update_pt_visit.drugAmt.data)
        pt.set_drug_qty(update_pt_visit.drugQty.data)
        pt.set_referral(update_pt_visit.referral.data)
        pt.set_consult_fee(update_pt_visit.consultFee.data)
        pt.set_total_fee(update_pt_visit.totFee.data)
        pt.set_claim(update_pt_visit.claim.data)
        pt.set_copayment(update_pt_visit.copayment.data)
        pt.set_cash(update_pt_visit.cashCollected.data)
        pt.set_remarks(update_pt_visit.remarks.data)
        pt.set_total_drugs(update_pt_visit.totalDrugs.data)
        pt.set_keep_date(keepDate)

        print(update_pt_visit.drugNameList.data)

        db['ptVisits'] = pt_visits
        db.close()

        return redirect(url_for('search_pt'))
    else:
        pt_visits = {}
        db = shelve.open('storage.db', 'r')
        pt_visits = db['ptVisits']
        db.close()

        pt = pt_visits.get(sig)
        update_pt_visit.ptName.data = pt.get_fullname()
        update_pt_visit.nric.data = pt.get_nric()
        update_pt_visit.visitDate.data = pt.get_keep_date()
        update_pt_visit.chargeType.data = pt.get_charge_type()
        update_pt_visit.allergies.data = pt.get_allergies()
        update_pt_visit.company.data = pt.get_company()
        update_pt_visit.mcDay.data = pt.get_mc_day()
        update_pt_visit.mcReason.data = pt.get_mc_reason()
        update_pt_visit.mcDate.data = pt.get_mc_date()
        update_pt_visit.priDiagnosis.data = pt.get_pri_diagnosis()
        update_pt_visit.secDiagnosis.data = pt.get_sec_diagnosis()
        update_pt_visit.drugNameList.data = pt.get_drug_list()
        update_pt_visit.drugPriceList.data = pt.get_drug_price_list()
        update_pt_visit.drugQtyList.data = pt.get_drug_qty_list()
        update_pt_visit.drugAmtList.data = pt.get_drug_amt_list()
        update_pt_visit.referral.data = pt.get_referral()
        update_pt_visit.consultFee.data = pt.get_consult_fee()
        update_pt_visit.totFee.data = pt.get_total_fee()
        update_pt_visit.claim.data = pt.get_claim()
        update_pt_visit.copayment.data = pt.get_copayment()
        update_pt_visit.cashCollected.data = pt.get_cash()
        update_pt_visit.remarks.data = pt.get_remarks()
        update_pt_visit.drugName.data = pt.get_drug_name()
        update_pt_visit.drugPrice.data = pt.get_drug_price()
        update_pt_visit.drugQty.data = pt.get_drug_qty()
        update_pt_visit.drugAmt.data = pt.get_drug_amt()
        update_pt_visit.totalDrugs.data = pt.get_total_drugs()

        drugNameList = pt.get_drug_list().split(',')
        drugPriceList = pt.get_drug_price_list().split(',')
        drugQtyList = pt.get_drug_qty_list().split(',')
        drugAmtList = pt.get_drug_amt_list().split(',')
        nric = pt.get_nric()
        for i in range(len(drugNameList)):
            if drugNameList[i] == '':
                drugNameList.pop(i)
        drugCount = len(drugNameList)
        keepDate = pt.get_keep_date()
        mcDate = pt.get_mc_date()
        print(drugNameList)
        print(drugCount)
        return render_template('updateVisit.html', form=update_pt_visit, drugNameList=drugNameList, drugPriceList=drugPriceList, drugQtyList=drugQtyList, drugAmtList=drugAmtList, drugCount=drugCount, e=0, keepDate=keepDate, mcDate=mcDate, nric=nric)

@app.route('/deleteVisit/<string:nric>')
def delete_visit(nric):
    pt_visits = {}
    db = shelve.open('storage.db', 'w')
    pt_visits = db['ptVisits']

    pt_visits.pop(nric)

    db['ptVisits'] = pt_visits
    db.close()

    return redirect(url_for('search_pt'))

# Clinic Side add visit
@app.route('/addVisit', methods=['GET', 'POST'])
def add_pt_visit():
    create_pt_visit = PtVisit(request.form)
    search = SearchVisits(request.form)
    if request.method == 'POST' and create_pt_visit.validate():

        pt_visits = {}
        db = shelve.open('storage.db', 'c')

        try:
            pt_visits = db['ptVisits']
        except:
            print("Error in retrieving ptVisits from storage.db.")

        keepDate = create_pt_visit.visitDate.data
        visit_date = (create_pt_visit.visitDate.data.strftime("%d %m %Y"))
        drugNameList = create_pt_visit.drugNameList.data
        drugPriceList = create_pt_visit.drugPriceList.data
        drugQtyList = create_pt_visit.drugQtyList.data
        drugAmtList = create_pt_visit.drugAmtList.data

        for i in range(len(drugNameList)):
            if drugNameList[i] == '':
                drugNameList.pop(i)

        global visit
        global addedThePt
        global displayedThePt
        addedThePt += 1
        visit = addVisit.addVisit(create_pt_visit.ptName.data, create_pt_visit.nric.data, visit_date, create_pt_visit.chargeType.data, create_pt_visit.priDiagnosis.data, create_pt_visit.cashCollected.data, create_pt_visit.company.data, create_pt_visit.allergies.data, create_pt_visit.mcDay.data, create_pt_visit.mcReason.data, create_pt_visit.mcDate.data, create_pt_visit.secDiagnosis.data, create_pt_visit.referral.data, create_pt_visit.claim.data, create_pt_visit.copayment.data, create_pt_visit.remarks.data, drugNameList, drugPriceList, drugQtyList, drugAmtList, create_pt_visit.clinic, create_pt_visit.totFee.data, create_pt_visit.consultFee.data, create_pt_visit.drugName.data, create_pt_visit.drugPrice.data, create_pt_visit.drugQty.data, create_pt_visit.drugAmt.data, create_pt_visit.totalDrugs.data, keepDate)
        pt_visits[visit.get_nric()] = visit # paste together for hash secure +visit.get_visit_date()+visit.get_clinic()
        db['ptVisits'] = pt_visits
        print(visit.get_keep_date())

        db.close()

        return redirect(url_for('search_pt', form=search, added=1, pt=create_pt_visit.ptName.data, visit=visit))
    return render_template('addVisit.html', form=create_pt_visit)

@app.route('/afterConsult/<string:sessionid>', methods=['GET', 'POST'])
def after_consult(sessionid):
    create_payment_form = Payment(request.form)
    db = shelve.open('storage.db', 'c')
    bookings = {}
    try:
        bookings = db['Bookings']
    except:
        print("Error in retrieving Bookings from storage.db.")
    print(bookings)
    return render_template('afterConsult.html', form=create_payment_form, ptBookings=bookings, session=sessionid)

if __name__ == '__main__':
    app.run()
