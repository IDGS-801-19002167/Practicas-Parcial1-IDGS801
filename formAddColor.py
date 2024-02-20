# WTF imports
from wtforms import Form
from wtforms import validators
from wtforms import StringField, TelField, IntegerField, RadioField
from wtforms import EmailField
from wtforms.validators import DataRequired, Email

# Flask imports
from flask_wtf import FlaskForm


class addColorForm(Form):
    ingles = StringField(
        "ingles",
        [
            validators.DataRequired(message="El campo es requerido"),
            validators.length(min=3, max=10, message="Ingresa un color en inglés"),
        ],
    )

    espanol = StringField(
        "espanol",
        [
            validators.DataRequired(message="El campo es requerido"),
            validators.length(min=4, max=10, message="Ingresa un color en español"),
        ],
    )


class searchColorForm(Form):
    buscar = StringField(
        "buscar",
        [
            validators.DataRequired(message="Ingresa un color para buscarlo"),
            validators.length(min=3, max=15, message="Ingresa un color para buscarlo"),
        ],
    )

    lang = RadioField(
        "Idioma",
        choices=[("ingles", "Inglés"), ("espanol", "Español")],
        validators=[validators.DataRequired(message="Selecciona un lenguaje")],
    )
