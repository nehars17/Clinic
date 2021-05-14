from wtforms import Form, StringField, RadioField, FloatField, IntegerField, DateField, SelectField, TextAreaField, BooleanField, validators
import shelve


class CreateConsultForm(Form):
    notes = TextAreaField('', [validators.Optional()])
    location = SelectField('', [validators.DataRequired()], choices=[('', 'Location'), ('AMK', 'Ang Mo Kio'), ('Bedok', 'Bedok'), ('Bishan', 'Bishan'), ('Changi', 'Changi'), ('Geylang', 'Geylang'), ('JurongE', 'Jurong East'), ('JurongW', 'Jurong West'), ('Punggol', 'Punggol'), ('Sembawang', 'Sembawang'), ('Sentosa', 'Sentosa'), ('Woodlands', 'Woodlands'), ('Yishun', 'Yishun')], default='')
    clinic = SelectField('', choices=[('', 'Select Location')], default='')
    searchClinic = StringField('', [validators.Optional()])
    nric = StringField('', [validators.DataRequired(), validators.Length(min=9, max=9, message="Enter a valid NRIC")])
    symptoms = StringField('', [validators.Optional()])
    fullname = StringField('', [validators.DataRequired()])

    date = StringField('', [validators.Optional()])
    timing = SelectField('', [validators.DataRequired()], choices=[('', 'Select'), ('0900-1000', '9am-10am'), ('1000-1100', '10am-11am'), ('1100-1200', '11am-12pm'), ('1200-1300', '12pm-1pm'), ('1300-1400', '1pm-2pm')], default='')

    # Find list of clinics depending on location
    def list_of_clinics(self, location):
        clinic_list = {}
        db = shelve.open('storage.db', 'c')

        try:
            clinic_list = db['ClinicList']
        except:
            print("Error in retrieving Users from storage.db.")

    """
    AMKClinic = SelectField()
    BedokClinic = SelectField()
    BishanClinic = SelectField()
    ChangiClinic = SelectField()
    GeylangClinic = SelectField()
    JEClinic = SelectField()
    JWClinic = SelectField()
    PunggolClinic = SelectField()
    SembawangClinic = SelectField()
    SentosaClinic = SelectField()
    WoodlandsClinic = SelectField()
    YishunClinic = SelectField()
    """


class SearchVisits(Form):
    searchBy = SelectField('Search By', [validators.Optional()], choices=[('Name', 'Patient Name'), ('NRIC', 'Patient NRIC'), ('visitno', 'Visit No')])
    searchFor = StringField('', [validators.Optional()])
    fromDate = StringField('Start Date', [validators.Optional()])
    toDate = StringField('End Date', [validators.Optional()])

class PtVisit(Form):
    ptName = StringField('', [validators.DataRequired(), validators.Length(min=3, max=70, message="Name must be between %(min)d and %(max)d characters.")])
    nric = StringField('', [validators.DataRequired()])
    allergies = StringField('', [validators.Optional()])
    company = StringField('', [validators.Optional()])
    chargeType = SelectField('', [validators.DataRequired()], choices=[('online', 'Online'), ('physical', 'Physical'), ('repeatMed', 'Repeat Medicine')], default='online')
    mcReason = SelectField('', [validators.Optional()], choices=[('', 'No MC'), ('diarrhea', 'Diarrhea'), ('migraine', 'Migraine'), ('spinePain', 'Spine Pain'), ('gastro', 'Gastroenteritis')], default='')
    priDiagnosis = SelectField('', [validators.DataRequired()], choices=[('', 'Must Enter a Diagnosis'), ('ache', 'Ache'), ('hyperlipids', 'Hyperlipidemia'), ('htn', 'Hypertension'), ('hbp', 'High Blood Pressure'), ('rashes', 'Rashes')], default='')
    secDiagnosis = SelectField('', [validators.Optional()], choices=[('', 'None'), ('ache', 'Ache'), ('hyperlipids', 'Hyperlipidemia'), ('htn', 'Hypertension'), ('hbp', 'High Blood Pressure'), ('rashes', 'Rashes')], default='')
    totalDrugs = FloatField('', [validators.Optional()])

    drugName = StringField('', [validators.Optional()])
    drugPrice = FloatField('', [validators.Optional()])
    drugQty = FloatField('', [validators.Optional()])
    drugAmt = FloatField('', [validators.Optional()])

    drugNameList = StringField('', [validators.Optional()])
    drugPriceList = StringField('', [validators.Optional()])
    drugQtyList = StringField('', [validators.Optional()])
    drugAmtList = StringField('', [validators.Optional()])

    referral = BooleanField('', [validators.Optional()])
    claim = FloatField('', [validators.Optional(), validators.NumberRange(min=0, message="Claim cant be less than 0.")])
    copayment = FloatField('', [validators.Optional(), validators.NumberRange(min=0, message="Copayment cant be less than 0.")])
    cashCollected = FloatField('', [validators.DataRequired(), validators.NumberRange(min=0, message="Cash cant be less than 0.")])
    remarks = TextAreaField('Remarks', [validators.Optional()])

    visitDate = DateField('Visit Date', [validators.Optional()])
    mcDate = DateField('', [validators.Optional()])
    clinic = ""
    # get from clinic login info (session data)
    totFee = FloatField('', [validators.Optional()])
    consultFee = FloatField('', [validators.Optional(), validators.NumberRange(min=0, message="Consultation Fee cant be less than 0.")])

    mcDay = FloatField('', [validators.Optional(), validators.NumberRange(min=0, message="Day cant be less than 0.")])

class Payment(Form):
    creditName = StringField('', [validators.DataRequired()])
