from flask import Flask,redirect,render_template
from flask_sqlalchemy import SQLAlchemy

#mydatabase connection
local_server=True
app=Flask(__name__)
app.secret_key="Revi"

#app.config['SQLALCHEMY_DATABASE_URI']='mysql://username:password@localhost/databasename'
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:@localhost/COVID'
db=SQLAlchemy(app)

class TEST(db.Model):
    ID=db.Column(db.Integer,primary_key=True)
    NAME=db.Column(db.String(20))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/UserSignup")
def UserSignup():
    return render_template("UserSignup.html")

#Testing whether database is connected or not
@app.route("/test")
def test():
    try:
        a=TEST.query.all()
        print(a)
        return 'MY Database is Connected'
    except Exception as e:
        print(e)
        return 'My Database is not connected {e}'
    
app.run(debug=True)


