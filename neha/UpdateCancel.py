from wtforms import Form, StringField, RadioField, SelectField, TextAreaField, validators
from wtforms.fields.html5 import DateField,EmailField,TimeField,IntegerField
class UpdateAndCancel(Form):
    name = StringField('Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    nric = StringField('NRIC', [validators.Length(min=9,max=9), validators.DataRequired()])
    email= EmailField('Email',[validators.Length(min=1, max=150), validators.DataRequired()])
    phone= StringField('Contact Number',[validators.Length(min=8,max=8), validators.DataRequired()])
    purpose = SelectField('Purpose', [validators.DataRequired()], choices=[('M', 'Medical Test/Examination'), ('D', 'Doctor Consultation'), ('C', 'Collection of Documents')], default='')
    date_of_arrival=DateField('Date', format='%Y-%m-%d')
    message = TextAreaField('Message (elaborate on condition or any symptoms)', [validators.Optional()])
    time= TimeField('Time',[validators.DataRequired()])
    clinic = SelectField('Choose Clinic', [validators.DataRequired()], choices=[('JD', 'JD Clinic - Ang Mo Kio'), ('H', 'Happy Clinic-Toa Payoh'), ('S', 'Sim\'s clinic- Serangoon')], default='')