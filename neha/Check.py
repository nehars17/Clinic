from wtforms import Form,BooleanField,validators

class checking(Form):
    checkbox=BooleanField('',[validators.DataRequired()])