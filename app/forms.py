from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, IntegerRangeField,FileField,SubmitField
from flask_wtf.file import FileAllowed
from werkzeug.datastructures import FileStorage
from wtforms.validators import DataRequired, Email

class New_Property(FlaskForm):
    title = StringField("Property Title",validators=[DataRequired()])
    description = TextAreaField("Description",validators=[DataRequired()])
    bedrooms = StringField("No. of Bedrooms",validators=[DataRequired()])
    bathrooms = StringField("No. of Bathrooms",validators=[DataRequired()])
    price = StringField("Price",validators=[DataRequired()])
    property_type = SelectField("Type", choices=[('appartment','Appartment'),('house','House')])
    location = StringField("Location",validators=[DataRequired()])
    photo = FileField("Browse", validators=[FileAllowed(['jpg','png'])])

class ContactForm(FlaskForm):
    name = StringField ('Name', validators=[DataRequired()])
    email = StringField ('Email', validators=[Email(), DataRequired()])
    subject = StringField ('Subject', validators=[DataRequired()])
    msg = TextAreaField ('Message', validators=[DataRequired()])
    submit = SubmitField('Send')