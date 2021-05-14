from wtforms import Form, validators
from wtforms.fields.html5 import DateField
class Schedule(Form):
    date = DateField('Enter Date', [validators.DataRequired()], format='%Y-%m-%d', )