# python 3
import pymysql
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
application = app

# connect to database when running app on web host
# change databaseuser (username), databasepassword (password), databasename
userpass = 'mysql+pymysql://databaseuser:databasepassword@'
basedir  = '127.0.0.1'
dbname   = '/databasename'


# put them all together as a string that shows SQLAlchemy where the database is
app.config['SQLALCHEMY_DATABASE_URI'] = userpass + basedir + dbname

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# this variable, db, will be used for all SQLAlchemy commands
db = SQLAlchemy(app)

# this route will test the database connection and nothing more
@app.route('/')
def testdb():
    try:
        db.session.query("1").from_statement("SELECT 1").all()
        return '<h1>It works.</h1>'
    except:
        return '<h1>Something is broken.</h1>'

if __name__ == '__main__':
    app.run(debug=True)
