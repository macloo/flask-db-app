# /Users/username/Documents/python/projectname/env/bin/python

#   change the path above to match yours

# using python 3
# this version has more routes - for insert, update, delete
import pymysql
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField, RadioField, HiddenField, StringField, IntegerField, FloatField
from wtforms.validators import InputRequired
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
    id_field = HiddenField('id')
    submit = SubmitField('Update This Record')

class DeleteChoiceForm(FlaskForm):
    id_field = HiddenField('id')
    submit = SubmitField('Delete This Record')

# form for add.html - insert new record
class AddRecord(FlaskForm):
    name = StringField('Sock name', [InputRequired()])
    style = SelectField('Choose the sock style', [InputRequired()],
    choices=[ ('', ''), ('ankle', 'Ankle'),
      ('knee-high', 'Knee-high'),
      ('mini', 'Mini'),
      ('other', 'Other') ])
    color = StringField('Color', [InputRequired()])
    quantity = IntegerField('Quantity in stock', [InputRequired()])
    price = FloatField('Retail price per pair', [InputRequired()])
    # updated is handled in route
    submit = SubmitField('Add This Record')

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

# this route is called by the form in index.html template
@app.route('/list', methods=['POST'])
def socklist():
    style = request.form['select']
    socks = Sock.query.filter_by(style=style).order_by(Sock.name).all()
    return render_template('list.html', style=style, socks=socks)

# whichever id is in the browser address bar, that one sock will be displayed
@app.route('/sock/<id>')
def sock(id):
    the_sock = Sock.query.filter_by(id=id).first_or_404()
    return render_template('sock.html', the_sock=the_sock)

# show all sock records in a table and get one record
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
        # if GET and no id received, do this
        socks = Sock.query.order_by(Sock.name).all()
        return render_template('table.html', socks=socks)
# above is pretty cool - the try command sends you to a different template
# if the form was submitted - or except, if it was not - see action= in
# the form element in table.html

# two routes - each opened by form sock.html
@app.route('/update', methods=['POST'])
def update():
    return "Update record"

@app.route('/delete', methods=['POST'])
def delete():
    # if POST and id received, do this
    id = request.form['id_field']
    the_sock = Sock.query.filter_by(id=id).first_or_404()
    form3 = DeleteChoiceForm()
    return render_template('delete_record.html', the_sock=the_sock, id=id, form3=form3)

@app.route('/result', methods=['POST'])
def result():
    # if POST and id received, do this
    id = request.form['id_field']
    the_sock = Sock.query.filter_by(id=id).first()
    sockname = the_sock.name
    result = "deleted"
    db.session.delete(the_sock)
    db.session.commit()
    return render_template('result.html', result=result, sockname=sockname)

# add a new sock to the database
@app.route('/add', methods=['GET', 'POST'])
def add():
    try:
        # if POST received, do this
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
    except:
        # if not POST, show empty form
        form3 = AddRecord()
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
