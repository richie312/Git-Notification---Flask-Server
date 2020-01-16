# -*- coding: utf-8 -*-

import flask
from flask import Flask, request, json,render_template
import webbrowser
from mail import *

app = Flask(__name__)
app.config['DEBUG'] = True

""" read the list of users"""
with open('users.txt','r') as readfile:
    email_list = readfile.readlines()

email_list = [email_list[i].replace('\n',"") for i in range(len(email_list))]

@app.route("/")        # Standard Flask endpoint
def homepage():
    return render_template("user_form.html")

@app.route("/delete")        # Standard Flask endpoint
def delete():
    return render_template("delete_user.html")


@app.route('/adduser', methods=['POST'])
def adduser():
    data = request.form
    with open('users.txt','a+') as outfile:
        outfile.write(data['Email Address'] + '\n')
    return render_template('user_form_response.html')

@app.route('/deleteuser', methods=['POST'])
def deleteuser():
    data = request.form
    with open('users.txt','r') as readfile:
        email_list = readfile.readlines()
    email_list = [email_list[i].replace('\n',"") for i in range(len(email_list))]
    email_list.remove(data['email_address'])    
    with open('users.txt','w') as outfile:
        outfile.write("\n".join(email_list))
    return render_template('user_form_response.html')

data = {"email_address": "richie.chatterjee31@gmail.com"}

	
@app.route('/get_github_notification',methods = ['POST'])
def get_github_notification():    
    response = request.json
    with open('response.json','w') as outfile:
        json.dump(response, outfile)
    file_list = ['changes_required.html','response.json']
    for i in range(len(email_list)):
        mailto(email_list[i],file_list)
    return json.dumps(request.json)

if __name__ == '__main__':
    app.run(host = '0.0.0.0',debug=True,port=5001)
