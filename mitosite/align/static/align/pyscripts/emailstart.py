import smtplib
from email.mime.text import MIMEText as text

def startalert(targadrs, randkey):

	fromaddr = "whb17@ic.ac.uk"
	toaddrs  = targadrs
	subject = 'HAMSTR job is in progress'

	msg = text("Dear user, \n \n Your HAMSTR job has initiated. \n \n Unique key: " + randkey + ". \n \n Check on the status of your job by inputting your key at the following link: \n \n http://ld-mjeste10.bc.ic.ac.uk:8000/ \n \n Love HAMSTRbot \n \n \n ### THIS IS AN AUTOMATED EMAIL ###" )

	msg['Subject'] = subject
	msg['From'] = fromaddr
	msg['To'] = toaddrs

	server = smtplib.SMTP('localhost')
	server.set_debuglevel(1)
	server.sendmail(fromaddr, toaddrs, msg.as_string())
	server.quit()
