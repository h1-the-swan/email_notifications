# coding: utf-8
from dotenv import load_dotenv
import smtplib
import os
load_dotenv(os.path.join(os.path.expanduser('~'), '.env'))
EMAIL_USERNAME = os.environ['EMAIL_NOTIFICATION_USERNAME']
EMAIL_PASSWORD = os.environ['EMAIL_NOTIFICATION_PASSWORD']
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
print(server.ehlo())
print(server.ehlo()[1])
server.starttls()
server.ehlo()
print(server.ehlo()[1])
server.login(EMAIL_USERNAME, EMAIL_PASSWORD)
server.ehlo()
from email.mime.text import MIMEText
msg = MIMEText(u'Test email from python')
msg['Subject'] = 'A test email sent from python'
msg['From'] = EMAIL_USERNAME
msg['To'] = 'jporteno@uw.edu'
get_ipython().magic(u'pinfo server.send')
get_ipython().magic(u'pinfo server.sendmail')
get_ipython().magic(u'pinfo server.sendmail')
server.sendmail(msg['From'], [msg['To']], msg.as_string())
server.quit()
