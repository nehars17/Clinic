from wtforms import Form, StringField, RadioField, SelectField, TextAreaField, validators, BooleanField

class CreatePrescriptionForm(Form):
    nric = StringField('NRIC', [validators.length(min=9, max=9), validators.DataRequired()])
    clinic = StringField('Clinic Name', [validators.DataRequired()])
    medication = TextAreaField('Medication', [validators.DataRequired()], )
    symptoms = TextAreaField('Symptoms', [validators.DataRequired()])
    instructions = TextAreaField('Instructions', [validators.DataRequired()])
    sideEffects = TextAreaField('Side Effects', [validators.DataRequired()])

class CreateReferral(Form):
    name = StringField('Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    nric = StringField('NRIC', [validators.Length(min=9, max=9), validators.DataRequired()])
    reason = TextAreaField('Reason for Referral', [validators.DataRequired()])
    organisation = TextAreaField('Hospital/Specialist Center Referred To', [validators.DataRequired()])
