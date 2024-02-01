# WTF imports
from wtforms import Form
from wtforms import StringField,TelField, IntegerField
from wtforms.validators import DataRequired, Email
from wtforms import EmailField

# Flask imports
from flask_wtf import FlaskForm

# Class
class CalculateForm(Form):
    number1 = IntegerField("number1")
    number2 = IntegerField("number2")
    number3 = IntegerField("number3")
    number4 = IntegerField("number4")
    
    