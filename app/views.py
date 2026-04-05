"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file contains the routes for your application.
"""
import os
from app import app, db
from flask import render_template, request, redirect, url_for, flash, session, abort, send_from_directory
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage
from app.models import Property
from app.forms import New_Property


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")


###
# The functions below should be applicable to all Flask apps.
###

def get_uploaded_images():
    rootdir = os.getcwd()
    print (rootdir)
    images = []
    for subdir, dirs, files in os.walk(rootdir + "/uploads"):
        for file in files:
            print (os.path.join(subdir, file))
            relative_path = os.path.relpath ((os.path.join(subdir, file)),(app.config["UPLOAD_FOLDER"]))
            images.append(relative_path)
    return images

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.route('/uploads/<filename>')
def get_images(filename):
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)

@app.route('/properties/create', methods=['GET','POST'])
def create ():

    form = New_Property()

    if form.validate_on_submit():
        img = form.photo.data
        filename = secure_filename(img.filename)
        filepath = os.path.join(app.config["UPLOAD_FOLDER"],filename)
        img.save(filepath)

        

        property = Property(
            title = form.title.data,
            description=form.description.data,
            bedrooms = form.bedrooms.data,
            bathrooms = form.bathrooms.data,
            location = form.location.data,
            price = str(form.price.data).replace(',', ''),
            property_type = form.property_type.data,
            photo=filename
                            )
        
        db.session.add(property)
        db.session.commit()

        flash('Property Successfully Saved', 'success')
        return redirect(url_for('properties'))
    flash_errors(form)
    return render_template('create.html', form=form)

@app.route('/properties',methods=['GET'])
def properties():
    properties = Property.query.all()
    return render_template('properties.html',properties=properties)

@app.route('/properties/<propertyid>')
def property_details(propertyid):
    property =  Property.query.get_or_404(propertyid)
    return render_template('property.html', property=property)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404
