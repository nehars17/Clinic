from flask import Flask, render_template, request, redirect, url_for,session
from Forms import CreateUserForm
from nehaUpdateCancel import UpdateAndCancel
from nehaSchedule import Schedule
import shelve,janineClass
from Check import checking

app = Flask(__name__)
global nric
nric=input('Enter NRIC:')

@app.route('/')
def home():
    return render_template('test.html')

@app.route('/Retrieve_Appointment')
def retrieve_appt():
    global nric
    patient_dict = []
    try:
        db = shelve.open('storage.db', 'r')
        patient_dict = db['Patient']
        db.close()
    except:
        print('Error in retrieving Patients from storage.db')
    public_db = shelve.open('public_storage.db', 'r')
    user_dict = public_db['Users']
    public_db.close()
    if nric in patient_dict:
        user = user_dict.get(nric)

    return render_template('Retrieve_Appointment.html',patient_dict=patient_dict)

@app.route('/confirmation/<int:patient_index>/')
def confirm(patient_index):
    global nric
    patient_dict = []

    try:
        db = shelve.open('storage.db', 'r')
        patient_dict = db['Patient']
        db.close()
    except:
        print('Error in Retrieving Patients from storage.db')


    public_db = shelve.open('public_storage.db', 'r')
    user_dict = public_db['Users']
    public_db.close()
    user_list=[]
    patient_list=[]

    user = user_dict.get(nric)
    patient=patient_dict[patient_index]
    patient_list.append(patient)

    user_list.append(user)

    return render_template('appointmentConfirmation.html',patient_list=patient_list,user_list=user_list)
# @app.route('/confirmation_update')
# def confirm_update():
#     patient_dict = {}
#     global nric
#     db = shelve.open('storage.db', 'r')
#     patient_dict = db['Patient']
#     db.close()
#     public_db = shelve.open('public_storage.db', 'r')
#     user_dict = public_db['Users']
#     public_db.close()
#     patient_list = []
#     user_list = []
#     if nric in patient_dict:
#         patient = patient_dict.get(nric)
#         patient_list.append(patient)
#         user = user_dict.get(nric)
#         user_list.append(user)
#
#         return render_template('confirmation_update.html',patient_list=patient_list,user_list=user_list)

@app.route('/confirmation_delete')
def confirm_delete():
    return render_template('confirmation_delete.html')

# @app.route('/createUser')
# def retreive_info():
#         public_dict = {}
#         db = shelve.open('public_storage.db', 'r')
#         public_dict = db['Users']
#         public_list = []
#         nric = 'S1234567B'
#         if nric in public_dict:
#             public = public_dict.get(nric)
#             public_list.append(public)
#
#         return render_template('createAppointment.html',public_list=public_list)



@app.route('/createUser', methods=['GET', 'POST'])
def create_user():
    create_user_form = CreateUserForm(request.form)
    global nric
    if request.method == 'POST' and create_user_form.validate():
        patient_dict = []

        db = shelve.open('storage.db', 'c')

        try:
            patient_dict = db['Patient']
        except:
            print("Error in retrieving Users from storage.db.")

        patient = janineClass.Patient(create_user_form.purpose.data, create_user_form.clinic.data,
                                      create_user_form.date_of_arrival.data, create_user_form.time.data,
                                      create_user_form.message.data)
        patient.set_nric(nric)
        patient_dict.append(patient)
        # global pt_id
        # pt_id=id
        db['Patient'] = patient_dict
        print(patient_dict)
        db.close()
        return redirect(url_for('retrieve_appt'))


    else:
        user_dict = {}
        public_db = shelve.open('public_storage.db', 'r')
        user_dict = public_db['Users']
        public_db.close()
        if nric in user_dict:
            user = user_dict.get(nric)
            create_user_form.name.data = user.get_name()
            create_user_form.nric.data = user.get_nric()
            create_user_form.email.data = user.get_email()
            create_user_form.phone.data = user.get_phone()




    return render_template('createAppointment.html', form=create_user_form)


@app.route('/Update/<int:patient_index>/', methods=['GET','POST'])
def update_cancel(patient_index):
    global nric
    updatecancel=UpdateAndCancel(request.form)
    if request.method=='POST' and updatecancel.validate():
        patient_dict = []
        db = shelve.open('storage.db', 'w')
        try:
            patient_dict = db['Patient']
        except:
            print('Error in Retrieving Patients from storage.db')
        patient=patient_dict[patient_index]
        patient.set_time(updatecancel.time.data)
        patient.set_date_of_arrival(updatecancel.date_of_arrival.data)
        patient.set_clinic(updatecancel.clinic.data)
        patient.set_purpose(updatecancel.purpose.data)
        patient.set_message(updatecancel.message.data)

        db['Patient'] = patient_dict
        db.close()
        return redirect(url_for('retrieve_appt'))
    else:
        user_dict = {}
        patient_dict={}
        patient_id=[]
        public_db = shelve.open('public_storage.db', 'r')
        user_dict = public_db['Users']
        public_db.close()
        db=shelve.open('storage.db','r')
        patient_dict=db['Patient']
        db.close()
        if nric in user_dict:
            user = user_dict.get(nric)
            patient=patient_dict[patient_index]
            updatecancel.name.data=user.get_name()
            updatecancel.nric.data = user.get_nric()
            updatecancel.email.data = user.get_email()
            updatecancel.phone.data=user.get_phone()
            updatecancel.message.data=patient.get_message()
            updatecancel.purpose.data=patient.get_purpose()
            updatecancel.clinic.data=patient.get_clinic()
            updatecancel.date_of_arrival.data=patient.get_date_of_arrival()
            updatecancel.time.data=patient.get_time()


    return render_template('updateAppointment.html',form=updatecancel)

@app.route('/Delete/<int:patient_index>')
def delete(patient_index):
    global nric
    patient_dict = []
    try:
        db = shelve.open('storage.db', 'w')
        patient_dict=db['Patient']
    except:
        print('Error in retrieving Patients from storage.db')

    patient_dict.pop(patient_index)

    db['Patient'] = patient_dict
    db.close()
    return redirect(url_for('confirm_delete'))



@app.route('/Schedule_date', methods=['GET', 'POST'])
def schedule():
    Schedule_date = Schedule(request.form)
    if request.method == 'POST' and Schedule_date.validate():
        patient_dict = []
        user_dict={}
        db = shelve.open('storage.db', 'r')
        patient_dict = db['Patient']
        db.close()
        public_db=shelve.open('public_storage.db','r')
        user_dict=public_db['Users']
        print(patient_dict)
        public_db.close()
        user_list=[]
        user=user_dict
        print(patient_dict[0].get_date_of_arrival())
        patient_date = patient_dict[0].get_date_of_arrival()
        patient_list=[]
        patient=[]
        if Schedule_date.date.data==patient_date:
            print('hi')
            patient_list.append(patient_dict[0].get_purpose())
            patient_list.append(patient_dict[0].get_time())
            patient_list.append(patient_dict[0].get_message())
            user_list.append(user)



        return render_template('schedule.html',count=len(patient_list),patient_list=patient_list,user_list=user_list)

    return render_template('Schedule_date.html',form=Schedule_date)


# @app.route('/schedule/<int:patient_index>',methods=['GET','POST'])
# def checking_now(patient_index):
#     checking_form=checking(request.form)
#     if request.method == 'POST' and checking_form.validate():
#         patient_dict = []
#         db = shelve.open('storage.db', 'w')
#         patient_dict = db['Patient']
#         patient = patient_dict.pop(id)
#         db['Patient'] = patient_dict
#         db.close()
#     return render_template('schedule.html', form=checking_form)

# @app.route('/schedule', methods=['GET','POST'])
# def check():
#     form=CreateUserForm(request.form)
#     patient_dict = []
#     user_dict = {}
#     db = shelve.open('storage.db', 'r')
#     patient_dict = db['Patient']
#     db.close()
#     public_db = shelve.open('public_storage.db', 'r')
#     user_dict = public_db['Users']
#     public_db.close()
#     user_list = []
#     user = user_dict.get(nric)
#     print(patient_dict[0].get_date_of_arrival())
#     patient_date = patient_dict[0].get_date_of_arrival()
#     user_list.append(user)
#     if request.method == 'POST' and form.validate():
#         db=shelve.open('storage.db','w')
#         patient_dict=db['Patient']
#         checkbox=form.checkbox.data[1:-1].split(',')
#         print(checkbox)
#     return render_template('schedule.html',form=form,count=len(patient_dict),patient_dict=patient_dict,user_list=user_list)
#


# @app.route('/schedule')
# def check():
#     patient_dict = {}
#     db = shelve.open('storage.db', 'r')
#     patient_dict = db['Patient']
#
#     patient_list = []
#     for key in patient_dict:
#         patient = patient_dict.get(key)
#         patient_list.append(patient)
#
#     return render_template('schedule.html', count=len(patient_list), patient_list=patient_list)

@app.route('/Patient_Profile/<int:patient_index>/')
def profile(patient_index):
    patient_dict = []
    global nric
    try:
        db = shelve.open('storage.db', 'r')
        patient_dict = db['Patient']
        db.close()
    except:
        print('Error in Retrieving Patients from storage.db')

    public_db = shelve.open('public_storage.db', 'r')
    user_dict = public_db['Users']
    public_db.close()
    user_list = []
    patient_list = []

    user=user_dict.get(nric)
    patient=patient_dict[patient_index]
    patient_list.append(patient)
    user_list.append(user)

    return render_template('scheduleDetails.html', patient_list=patient_list,user_list=user_list)





if __name__ == '__main__':
    app.run()
