print("Starting test")

import subprocess
import time
import smtplib
import requests
import json

deviceList = []
nameList = []

def getIPs():
    f = open("/home/fpp/media/config/co-universes.json","r")
    data = json.load(f)
    for i in data['channelOutputs']:
        for j in i['universes']:
            #print(j['address'])
            if j['active']==1:
                #print(j['address'])
                deviceList.append(j['address'])
                nameList.append(j['description'])
    f.close()

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
    print("Checking...")
    fail = 0
    count = 0
    list = ""
    getIPs()
    for x in deviceList:
        success = ping(x)
        if success == 1:
            print (x+" Device Up")             # for debug
        else:
            print (x+" Device Not Responding")           # for debug
            list += nameList[count]+" "+x+"\r"
            fail += 1
        count +=1
    if fail>0:
        print("Sending email")		#for debug
        email(list)

checkDevices()
