#!/usr/bin/python3

import subprocess
import time
import smtplib
import json

f = open("../config/co-universes.json")
data = json.load(f)
deviceList = []
for i in data['channelOutputs']:
    for j in i['universes']:
        if j['active']==1:
            deviceList.append(j['address'])

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

##########################################################################
# UPDATE THESE WITH YOUR PERSONAL INFORMATION

def email(args):
    email_user = ""		# gmail account user name
    email_password = ""		# gmail account password ***THIS REQUIRES AN APP PASSWORD - SEE GOOGLE FOR DETAILS***
    email_send = ""		# email recipient
    subject = "Show Device(s) Down"		# email subject line
    body = "ALERT, a show device or devices are not responding\r\r"+args		# email body text

##########################################################################
    msg = MIMEMultipart()
    msg["From"] = email_user
    msg["To"] = email_send
    msg["Subject"] = subject

    msg.attach(MIMEText(body,"plain"))

    text = msg.as_string()
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(email_user,email_password)


    server.sendmail(email_user,email_send,text)
    server.quit()

def ping(site):

    cmd = "/bin/ping -c 1 " + site
    try:
        output = subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True)
    except subprocess.CalledProcessError:
        return 0
    else:
        return 1


def checkDevices():
    fail = 0
    list = ""
    for x in deviceList:
        success = ping(x)
        if success == 1:
            print (x+" Device Up")		# for debug

        else:
            print (x+" Device Not Responding")		# for debug
            list += x+"\r"
            fail += 1

    if fail>0:
        print("sending email")		#for debug
        email(list)

checkDevices()
