import smtplib
from email.mime.multipart import MIMEMultipart

#Complete the 3 variables below
gmail_user = 'gmail email id here'  
gmail_password = 'gmail password here'
recipient_email = 'Recipient email Address here'


try:  
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(gmail_user, gmail_password)
except:  
    print ('Something went wrong...')

msg = MIMEMultipart() 


msg['From']= gmail_user
msg['To']= recipient_email
msg['Subject']= 'Test Email'

try:
	server.send_message(msg)
except Exception as e:
	print ('Raised Exception while sending')

server.quit()
print ('Done')