from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, IntegerRangeField,FileField
from flask_wtf.file import FileAllowed
from werkzeug.datastructures import FileStorage
from wtforms.validators import DataRequired

class New_Property(FlaskForm):
    title = StringField("Property Title",validators=[DataRequired()])
    description = TextAreaField("Description",validators=[DataRequired()])
    bedrooms = StringField("No. of Bedrooms",validators=[DataRequired()])
    bathrooms = StringField("No. of Bathrooms",validators=[DataRequired()])
    price = StringField("Price",validators=[DataRequired()])
    property_type = SelectField("Type", choices=[('appartment','Appartment'),('house','House')])
    location = StringField("Location",validators=[DataRequired()])
    photo = FileField("Browse", validators=[FileAllowed(['jpg','png'])])
