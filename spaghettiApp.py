from flask import Flask, render_template, url_for, request, redirect, flash, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.utils import secure_filename
import os
import subprocess

UPLOAD_FOLDER = 'static'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///prints.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# db = SQLAlchemy(app)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

"""
class printPhoto(db.Model): # Feel free to add more attributes as y'all see fit
    id = db.Column(db.Integer, primary_key=True)
    path = db.Column(db.String(200), nullable=False)
    status = db.Column(db.Integer, default=0)   # Stringing or not stringing
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return '<Task %r>' % self.id
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


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            return render_template('home.html', message="Please select a file.")
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            return render_template('home.html', message="Please select a file.")
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            os.system('cp static/' + filename + ' /Users/ethannguyen/Desktop/College/SyBBURE/2020\ Summer/darknet/')
            os.system('cd ..; cd darknet; ./darknet detect cfg/model.cfg model.weights ' + filename)
            os.system('cp /Users/ethannguyen/Desktop/College/SyBBURE/2020\ Summer/darknet/predictions.jpg /Users/ethannguyen/Desktop/College/SyBBURE/2020\ Summer/VHacksSummer/static/' + filename)
            status = "Spaghetti"    # Get status from machine
            img = os.path.join(app.config['UPLOAD_FOLDER'], filename) # Put location of image returned by machine here
            return render_template('upload.html', img=img, status=status)
            # return redirect(url_for('uploaded_file',
            #                         filename=filename))
    return render_template('home.html', message="Upload")

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               'predictions.jpg')

if __name__ == "__main__":
    app.run(debug=True)