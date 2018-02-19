import smtplib
from email.mime.text import MIMEText as text
from mitositefuncs import *

def alertinput():

	def jobalert(targadrs):

		fromaddr = "whb17@ic.ac.uk"
		toaddrs  = targadrs
		subject = 'HAMSTR job complete'


		#key = keygen()

		msg = text("Dear user, \n \n HAMSTR job has finished. \n \n Unique key: " + {{random_key}} + ". \n \n Retrieve your job at the following link: \n \n http://ld-mjeste10.bc.ic.ac.uk:1337/ \n \n Love HAMSTRbot \n \n \n ### THIS IS AN AUTOMATED EMAIL ###" )

		msg['Subject'] = subject
		msg['From'] = fromaddr
		msg['To'] = toaddrs

		server = smtplib.SMTP('localhost')
		server.set_debuglevel(1)
		server.sendmail(fromaddr, toaddrs, msg.as_string())
		server.quit()


	recipient = input('Input recipient email address: ') # User must input recipient email address. Change to input handed off from django.
	number = input('Send how many times? ') # Be careful with this
	count = 1

	while count <= int(number):
		jobalert(recipient)

		count += 1

alertinput()