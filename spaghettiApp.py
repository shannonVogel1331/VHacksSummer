from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///prints.db'
db = SQLAlchemy(app)

class printPhoto(db.Model): # Feel free to add more attributes as y'all see fit
    id = db.Column(db.Integer, primary_key=True)
    path = db.Column(db.String(200), nullable=False)
    status = db.Column(db.Integer, default=0)   # Stringing or not stringing
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return '<Print %r>' % self.id

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        img_path = request.form['content']  # Have this reference an upload form
        print_status = ""   # Machine output here
        new_print = printPhoto(path=img_path, status=print_status)

        try:
            db.session.add(new_print)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue adding your task'

    else:
        prints = printPhoto.query.order_by(printPhoto.date_created).all()
        return render_template('home.html', prints=prints)

@app.route('/troubleshoot')
def troubleshoot():
    try:
        return redirect('/troubleshoot')
    except:
        return 'There was a problem redirecting'