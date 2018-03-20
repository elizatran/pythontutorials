import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

fromadd = 'eliza175@gmail.com'
toaddr = 'hanhdungtran@gmail.com'
text = 'text message sent from python'
username ='eliza175'
password = 'Dung1982'
msg = MIMEMultipart()
msg['From']= fromadd
msg['To'] = toaddr
msg['Subject'] = 'Test'
msg.attach(MIMEText(text))
server = smtplib.SMTP('smtp.gmail.com:507')
server.ehlo()
server.starttls()
server.ehlo()
server.login(username, password)
server.sendmail(fromadd, toadd, msg.as_tring())
server.quit()
