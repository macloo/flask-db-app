#!/Users/username/Documents/python/foldername/env/bin/python

#   change the path above to match yours

# using python 3
# this version has more routes - for insert, update, delete
# added WTF form validation
import pymysql
from flask import Flask, render_template, request, flash
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField, RadioField, HiddenField, StringField, IntegerField, FloatField
from wtforms.validators import InputRequired, Length, Regexp, NumberRange
from flask_sqlalchemy import SQLAlchemy
from datetime import date

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!sauce'

# connect to local database
userpass = 'mysql+pymysql://root:@'
basedir  = '127.0.0.1'
dbname   = '/sockmarket'
socket   = '?unix_socket=/Applications/XAMPP/xamppfiles/var/mysql/mysql.sock'
dbname   = dbname + socket

# setup required for SQLAlchemy and Bootstrap
app.config['SQLALCHEMY_DATABASE_URI'] = userpass + basedir + dbname

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

bootstrap = Bootstrap(app)
app.config['BOOTSTRAP_SERVE_LOCAL'] = True

db = SQLAlchemy(app)


# each table in the database needs a class to be created for it
# this db has only one table, socks
class Sock(db.Model):
    __tablename__ = 'socks'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    style = db.Column(db.String)
    color = db.Column(db.String)
    quantity = db.Column(db.Integer)
    price = db.Column(db.Float)
    updated = db.Column(db.String)

    def __init__(self, name, style, color, quantity, price, updated):
        self.name = name
        self.style = style
        self.color = color
        self.quantity = quantity
        self.price = price
        self.updated = updated

    def __repr__(self):
        return '<Sock %s>' % self.name

# Flask-WTF form magic
# form for index.html
class SockForm(FlaskForm):
    select = SelectField('Choose a sock style:',
      choices=[ ('ankle', 'Ankle'),
      ('knee-high', 'Knee-high'),
      ('mini', 'Mini'),
      ('other', 'Other') ])
    submit = SubmitField('Submit')

# two forms for sock.html - they submit to different routes
class UpdateChoiceForm(FlaskForm):
    id_field = HiddenField()
    purpose = HiddenField()
    submit = SubmitField('Update This Record')

class DeleteChoiceForm(FlaskForm):
    id_field = HiddenField()
    purpose = HiddenField()
    submit = SubmitField('Delete This Record')

# form for add.html - insert new record - and also update_record.html
# each field includes validation requirements and messages
class AddRecord(FlaskForm):
    id_field = HiddenField()
    name = StringField('Sock name', [ InputRequired(),
        Regexp(r'^[A-Za-z\s\-\']+$', message="Invalid sock name"),
        Length(min=3, max=25, message="Invalid sock name length")
        ])
    style = SelectField('Choose the sock style', [ InputRequired()],
        choices=[ ('', ''), ('ankle', 'Ankle'),
        ('knee-high', 'Knee-high'),
        ('mini', 'Mini'),
        ('other', 'Other') ])
    color = StringField('Color', [ InputRequired(),
        Regexp(r'^[A-Za-z\s\-\'\/]+$', message="Invalid color"),
        Length(min=3, max=25, message="Invalid color length")
        ])
    quantity = IntegerField('Quantity in stock', [ InputRequired(),
        NumberRange(min=1, max=999, message="Invalid range")
        ])
    price = FloatField('Retail price per pair', [ InputRequired(),
        NumberRange(min=1.00, max=99.99, message="Invalid range")
        ])
    updated = HiddenField()
    # updated is handled in route
    submit = SubmitField('Add/Update Record')

# get local date - does not account for time zone
def stringdate():
    today = date.today()
    date_list = str(today).split('-')
    date_string = date_list[1] + "-" + date_list[2] + "-" + date_list[0]
    return date_string

# ------------------------------------------------
# routes

# starting page for app
@app.route('/', methods=['GET'])
def index():
    form = SockForm()
    return render_template('index.html', form=form)

# list of socks by style - called by the form in index.html template
@app.route('/list', methods=['POST'])
def socklist():
    style = request.form['select']
    socks = Sock.query.filter_by(style=style).order_by(Sock.name).all()
    return render_template('list.html', style=style, socks=socks)

# display one sock record using the id in the browser address bar
@app.route('/sock/<id>')
def sock(id):
    the_sock = Sock.query.filter_by(id=id).first_or_404()
    return render_template('sock.html', the_sock=the_sock)

# show all sock records in a table - radio buttons to select one record
@app.route('/socks', methods=['GET', 'POST'])
def sock_table():
    try:
        # if POST and id received, do this
        id = request.form['id']
        the_sock = Sock.query.filter_by(id=id).first_or_404()
        # two forms - so they can be submitted to different routes
        form1 = UpdateChoiceForm()
        form2 = DeleteChoiceForm()
        return render_template('sock.html', the_sock=the_sock, id=id, form1=form1, form2=form2)
    except:
        # if GET and/or no id received, do this
        socks = Sock.query.order_by(Sock.name).all()
        return render_template('table.html', socks=socks)
# above is pretty cool - the try command sends you to a different template
# if the form was submitted - or except, if it was not - see action= in
# the form element in table.html

# two routes - each opened by form sock.html
@app.route('/update', methods=['POST'])
def update():
    # if POST and id received, provide filled-in form to edit
    id = request.form['id_field']
    the_sock = Sock.query.filter_by(id=id).first()
    form3 = AddRecord(obj=the_sock)
    return render_template('update_record.html', the_sock=the_sock, id=id, form3=form3)

@app.route('/delete', methods=['POST'])
def delete():
    # if POST and id received, ask for confirmation to delete
    id = request.form['id_field']
    the_sock = Sock.query.filter_by(id=id).first()
    form2 = DeleteChoiceForm()
    return render_template('delete_record.html', the_sock=the_sock, id=id, form2=form2)

# handle the update when form is submitted
@app.route('/update_result', methods=['POST'])
def update_result():
    id = request.form['id_field']
    the_sock = Sock.query.filter_by(id=id).first()
    sockname = the_sock.name
    purpose = 'updated'
    form3 = AddRecord()
    if form3.validate_on_submit():
        # update the db sock record with form values
        the_sock.name = request.form['name']
        the_sock.style = request.form['style']
        the_sock.color = request.form['color']
        the_sock.quantity = request.form['quantity']
        the_sock.price = request.form['price']
        # get today's date from function, above all the routes
        the_sock.updated = stringdate()
        # update database record
        db.session.commit()
        return render_template('result.html', result=purpose, sockname=sockname)
    else:
        # display error messages while keeping newly entered values
        # obtained from the form itself, not from the db
        flash('placeholder')
        the_sock.id = id
        the_sock.name = form3.name.data
        the_sock.style = form3.style.data
        the_sock.color = form3.color.data
        the_sock.quantity = form3.quantity.data
        the_sock.price = form3.price.data
        return render_template('update_record.html', form3=form3, the_sock=the_sock)

# perform the deletion of one sock record
@app.route('/deletion_result', methods=['POST'])
def deletion_result():
    id = request.form['id_field']
    purpose = request.form['purpose']
    the_sock = Sock.query.filter_by(id=id).first()
    sockname = the_sock.name
    if purpose == 'deleted':
        db.session.delete(the_sock)
        db.session.commit()
    else:
        # if value of purpose was other than expected
        return render_template('405.html'), 405
    return render_template('result.html', result=purpose, sockname=sockname)

# add a new sock to the database
@app.route('/add', methods=['GET', 'POST'])
def add():
    form3 = AddRecord()
    if form3.validate_on_submit():
        name = request.form['name']
        style = request.form['style']
        color = request.form['color']
        quantity = request.form['quantity']
        price = request.form['price']
        # get today's date from function, above all the routes
        updated = stringdate()
        # the data to be inserted into Sock model - the table, socks
        record = Sock(name, style, color, quantity, price, updated)
        # Flask-SQLAlchemy magic adds record to database
        db.session.add(record)
        db.session.commit()
        # create a message to send to the template
        message = "The data for sock %s has been submitted." % (name)
        return render_template('add.html', message=message)
    else:
        # show validaton errors
        flash('placeholder')
        return render_template('add.html', form3=form3)

# ------------------------------------------------
# error handlers

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(405)
def form_not_posted(e):
    return render_template('405.html'), 405

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(debug=True)
