import re
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///form.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)

class DatabaseEntry(db.Model):
    sno=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(50),nullable=False)
    email=db.Column(db.String(100),nullable=False)
    createdTime=db.Column(db.DateTime,nullable=True,default=datetime.utcnow)

    def __repr__(self) -> str:
        return f'{self.sno} -> {self.Name}'

@app.route("/", methods=['GET','POST'])
def hello_world():
    if request.method=='POST':
        name=request.form['name']
        email=request.form['email']
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if(re.fullmatch(regex, email)):
            database=DatabaseEntry(name=name,email=email)
            db.session.add(database)
            db.session.commit()
            mess='Form Submitted successfully'
            
            return render_template('index.html',mess=mess)
    
    mess=None

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)