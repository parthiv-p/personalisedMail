import smtplib
from email.mime.multipart import MIMEMultipart
import pandas as pd

#Complete the 2 variables below
gmail_user = ''  
gmail_password = ''

df = pd.read_csv('data.csv')
recipients = df['Recipients']
sendCount = 0

try:  
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(gmail_user, gmail_password)
except:  
    print ('Something went wrong...')


for sendCount, recipient in enumerate(recipients):
	
	msg = MIMEMultipart() 

	msg['From']= 'gmail_user'
	msg['To']= recipient
	msg['Subject']= 'Test Email' + str(sendCount)

	try:
		server.send_message(msg)
		sendCount += 1
		print ('Sent mail to {}'.format(recipient))
		del msg
	except Exception as e:
		print ('Raised Exception while sending mail to {}'.format(recipient))

server.quit()
print ('{} mails sent'.format(sendCount))