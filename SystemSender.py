import smtplib
import csv
import os
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.header import Header
#from email import Utils
#from email import Encoders


##  For SendMai Gsmtp login
rp_smtp = "smtp.gmail.com"
rp_port = "587"
user_id = "ddiagram4011@gmail.com"
user_passwd = "k20504003"

file = open("Duty02.txt", "r")
Document = MIMEText(file.read(),_charset='utf-8')
file.close()

# Duty Engineer Call List File Open

def send_mail(from_user, to_user, cc_manager, subject, informtext, attach):
    COMMASPACE = "," 
    msg = MIMEMultipart("alternative")
    msg["from"] = from_user
    msg["to"] = to_user
    msg["cc"] = COMMASPACE.join(cc_manager)
    msg["subject"] = Header(s=subject, charset="utf-8")
    msg.attach(Document)
    
    

    if (attach != None):
        rpset = MIMEBase("application","octet-stream")
        rpset.set_payload(open(attach,"rb").read())
        rpset.add_header("Content-Disposition","attachment; filename=Duty01.txt")
        msg.attach(rpset) 
     
    smtp = smtplib.SMTP(rp_smtp,rp_port)
    smtp.ehlo()
    smtp.starttls()
    smtp.login(user_id,user_passwd)
    smtp.sendmail(from_user, cc_manager, msg.as_string())
    smtp.quit()


send_mail('ddiagram4011@gmail.com', 'dhdiagram@gmail.com' , ['dohyoung.kim@rockplace.co.kr','hesigner@naver.com'] , "DutyEngineerCallMailer" , "TEST0000" ,'/opt/rockplace/bin/DutyMail/Duty01.txt')


