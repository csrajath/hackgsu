#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 15:25:08 2020

@author: nikhil
"""

from flask import Flask, request, render_template, send_from_directory
import requests
from api import mydb, seekers

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route("/")
def homepage():
    return render_template('index.html')

@app.route("/login/", methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    # users = mydb.db.users
    # login_user = users.find_one({'name': request.form['username']})
    # if login_user:

@app.route("/upload/")
def uploadresume():
    return render_template('student_resume_upload.html')

@app.route("/submit-profile/")
def userprofile():
    return render_template('student_profile_form.html')

@app.route("/formsubmitted/")
def usersubmission():
    return render_template('student_submitted.html')

if __name__ == "__main__":
    app.run(debug=False)
