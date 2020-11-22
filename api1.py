import requests, pyodbc, pymongo, json, os
from flask import Flask, request, redirect, url_for, render_template, send_from_directory, Response
from werkzeug.utils import secure_filename
from PyPDF2 import PdfFileReader, PdfFileWriter
import PyPDF2
import io
from urllib import request
from urllib.request import urlopen
import urllib
import json
from flask import Flask, request
# from flask.ext import restful
# from flask.ext.restful import reqparse
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
# from StringIO import StringIO
import os
from flask import Flask, request, jsonify
# from flask_restful import Resource, Api
from flask import make_response

# mongodb setup
uri = "mongodb://hackgsu:moqcCeQKiGDZVqYkqchqXtFcDMzxWD3p9MBbIZj2F3GaLaeSAQqu487LW6TCZYLGfuKOFxNl68EKyEmrCGu9fg==@hackgsu.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&maxIdleTimeMS=120000&appName=@hackgsu@"
client = pymongo.MongoClient(uri)
mydb = client["hackgsu"]   
seekers = mydb["seekers"] # seekers consists of job seekers info

UPLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__)) + '/uploads/'
DOWNLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__)) + '/downloads/'
ALLOWED_EXTENSIONS = {'pdf'}

app = Flask(__name__)
DIR_PATH = os.path.dirname(os.path.realpath(__file__))
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['DOWNLOAD_FOLDER'] = DOWNLOAD_FOLDER
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['MAX_CONTENT_LENGTH'] = 4 * 1024 * 1024

CVDetails = {'name':'John', 'education':'Bachelor of Science in Computer Science', 'skills':'Python, Hadoop,Mapreduce, AWS', 'Phone Number': '+1 404 124 3214', 'experience': 'Software Engineering Intern, CNN Corporation: \n Built a data pipeline to routinely collect data from Twitter, LexisNexis and Facebook APIs and store them in a Hadoop file cluster via Apache Kafka then migrated codes to AWS. \n Deployed a CNN deep neural network to classify relevant tweets with high accuracy. \nApplied various Topic Modeling techniques, Sentiment Analysis and other descriptive statistics on the extracted data and visualized them using Tableau.'}

@app.route('/details-form/', methods=['GET', 'POST'])
def formsubmission():
    return render_template('student_profile_form.html')

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload/', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        if 'file' not in request.files:
            print('No file attached in request')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            print('No file selected')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            return CVDetails
            # pdfFileObj = request.files['file']                 
            # pdfReader = PyPDF2.PdfFileReader(pdfFileObj)  
            # pageObj = pdfReader.getPage(0)  
            # print(pageObj.extractText()) 
            # pdfFileObj.close()
            # filename = secure_filename(file.filename)
        else:
            print('Upload a pdf file only') # TODO: Send this message to UI
    return render_template('student_resume_upload.html')

# def convert_pdf_to_txt(path):
#     return print(path)

# @app.route('/resume_parser', methods=['GET'])
# def resume_parser():
#     # takes a pdf file as input and returns a json file
#     return 'a'
# def process_file(path, filename):
#     generate_details(path, filename)


# @app.route('/jd_parser', methods=['POST'])
# def jd_parser():
#     print('1')
#     skills = ['machine learning', 'python', 'c++','java','tensorflow','aurdino','keras','deep learning','ios','android','html','css','javascript','aws','azure','powerbi']
#     jd = request.data.decode('utf-8')
#     print(jd)

#     skills_in_jd = []

#     for skill in skills:
#         if(skill in jd):
#             skills_in_jd.append(skill)
    
#     applications = seekers.find()

#     table_entries = []
#     for application in applications:
#         mydict = {}
#         score = 0
#         candidate_skills = application['skills'].split(',')
#         for skill in skills_in_jd:
#             if(skill in candidate_skills):
#                 score += 1
#         mydict['score'] = score
#         mydict['ph_no'] = application['phone']
#         mydict['skills'] = application['skills']
#         mydict['education'] = application['education']
#         mydict['work_exp'] = application['work_exp']
#         table_entries.append(mydict)


#     sorted_entries = sorted(table_entries, key = lambda i: i['score'],reverse=True)

#     return Response(response=json.dumps(sorted_entries), status=200, mimetype='application/json') 

if __name__ == "__main__":
    app.run(debug=True)
