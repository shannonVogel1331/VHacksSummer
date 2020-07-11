from flask import Flask, render_template, url_for, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///prints.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class printPhoto(db.Model): # Feel free to add more attributes as y'all see fit
    id = db.Column(db.Integer, primary_key=True)
    path = db.Column(db.String(200), nullable=False)
    status = db.Column(db.Integer, default=0)   # Stringing or not stringing
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return '<Task %r>' % self.id


@app.route('/', methods=['POST', 'GET'])
def home():
    return render_template('home.html')

"""
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
"""

@app.route('/troubleshootFailed')
def troubleshootFailed():
    try:
        return render_template('troubleshootingFailed.html')
    except:
        return 'There was a problem redirecting'

@app.route('/troubleshootQuality')
def troubleshootQuality():
    try:
        return render_template('troubleshootingQuality.html')
    except:
        return 'There was a problem redirecting'


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect('/')

        f = request.files['the_file']
        if file.filename == '':
            flash('No selected file')
            return redirect('/')

        f.save('/var/www/uploads/' + secure_filename(f.filename))

        return ""

if __name__ == "__main__":
    app.run(debug=True)