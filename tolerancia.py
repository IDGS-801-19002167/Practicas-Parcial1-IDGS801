# WTF imports
from wtforms import Form
from wtforms import StringField,TelField, IntegerField, SelectField, RadioField
from wtforms.validators import DataRequired, Email
from wtforms import EmailField

# Flask imports
from flask_wtf import FlaskForm

# Class
class toleranciaForm(Form):
    banda1 = SelectField("banda1")
    banda2 = SelectField("banda2")
    banda3 = SelectField("banda3")
    rdo = RadioField("rdo")
    