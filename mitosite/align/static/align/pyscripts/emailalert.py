import smtplib
from email.mime.text import MIMEText as text

with open('key.txt') as key:
	key = key.read()
	#print(key)

	with open('mailadrs.txt') as mailadrs:
		mailadrs = mailadrs.read()
		#print(mailadrs)


		def endalert(targadrs, key):

			fromaddr = "whb17@ic.ac.uk"
			toaddrs  = targadrs
			subject = 'HAMSTR job complete'

			msg = text("Dear user, \n \n HAMSTR job has finished. \n \n Unique key: " + key + ". \n \n Retrieve your job at the following link: \n \n http://ld-mjeste10.bc.ic.ac.uk:1337/ \n \n Love HAMSTRbot \n \n \n ### THIS IS AN AUTOMATED EMAIL ###")

			msg['Subject'] = subject
			msg['From'] = fromaddr
			msg['To'] = toaddrs

			server = smtplib.SMTP('localhost')
			server.set_debuglevel(1)
			server.sendmail(fromaddr, toaddrs, msg.as_string())
			server.quit()

		endalert(mailadrs, key)
