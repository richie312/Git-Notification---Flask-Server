import os, smtplib, ssl, getpass
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.base import MIMEBase
from email import encoders as Encoders
import getpass
import json
from decrypt import *
import os
port = 465

with open(r'auth/key_user.txt', 'r') as readfile:
    key_user = json.load(readfile)
with open(r'auth/user.txt', 'r') as readfile:
    user = json.load(readfile)
with open(r'auth/key_password.txt', 'r') as readfile:
    key_panda = json.load(readfile)
with open(r'auth/password.txt', 'r') as readfile:
    panda = json.load(readfile)

def send_mail(username, password, from_addr, to_addrs, msg):
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", port,context=context) as server:
        server.login(username, password)
        server.sendmail(from_addr, to_addrs, msg.as_string())

def mailto(email_address,file_list):
    username = decrypt(eval(user),eval(key_user)).decode("utf-8")
    password  = decrypt(eval(panda),eval(key_panda)).decode("utf-8") 
    fromaddr = username
    Body =   """<!DOCTYPE html>
                <html>
                <head>
                <style>
                body {
                        color: red;
                }
                h4 {
                        color: #1E162F;
                        font-size: 20px;
                }
                h5 {
                        color: rgb(0,0,255);
                        font-size: 15px;
                }
                
                p {
                        color: rgb(0,0,255)
                }
                </style>
                </head>
                <body>
                 
                <h4>Skillz-SphereEngine Integration Lab</h4>
                 
                </body>
                </html>
                """
    
    
    Body += u'<h5> Hi {name},</h5>'.format(name=email_address.split('@')[0])           
    Body += u'''<p>Skillz-SphereEngine Integration Lab has new commit available.</p>
                <li>Please pull the new code base from repo.</li>
                <li>Please find the change details in attached response.json file.</li>
                <li>Please find the changes required in the attachment.</p>
               '''

    msg = MIMEMultipart()
    Mail_Body=MIMEText(Body, 'html')
    msg.attach(Mail_Body)
    msg['From'] = username
    msg['To'] = email_address
    msg['Subject'] = "Skillz-SphereEngine Integration Lab"
    """Attach the file"""
    for f in file_list:  # add files to the message
        file_path = os.path.join(os.getcwd(), f)
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(open(file_path, 'rb').read())
        #attachment = MIMEApplication(open(file_path, "rb").read(), _subtype="txt")
        part.add_header('Content-Disposition','attachment', filename=f)
        part.add_header('Content-Disposition', 'attachment; filename="%s"' % f)    
        Encoders.encode_base64(part)
        msg.attach(part)
    send_mail(username=username, password=password, from_addr=fromaddr, to_addrs=email_address, msg=msg)
