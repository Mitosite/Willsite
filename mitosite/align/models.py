from django.db import models
from django.forms import ModelForm

'''
class SingleJob(models.Model):
	#User uploaded fastq file
	readsfile = models.FileField(default='/project/home17/whb17/public_html/randtestreads.fasta')
	#adapters to be typed into textbox
	#adapters = models.CharField(null=True, max_length=50)
	#user's email address
	user_email = models.EmailField(default='whb17@ic.ac.uk')
	#10-digit randomly generated key
	#key = models.CharField(max_length=50)


class PairedJob(models.Model):
	readsfile1 = models.FileField(null=True)
	readsfile2 = models.FileField(null=True)
	adapters = models.CharField(null=True, max_length=50)
	key = models.CharField(null=True, max_length=50)
'''

class UploadFile(models.Model):
	#title = models.CharField(max_length=50, default='sample')
	file = models.FileField(default='/project/home17/whb17/public_html/randtestreads.fasta')
	user_email = models.EmailField(default='whb17@ic.ac.uk')
	randkey = models.CharField(max_length=101, default=10*'0')

