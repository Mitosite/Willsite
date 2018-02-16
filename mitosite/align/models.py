from django.db import models
from django.forms import ModelForm


class Singlejob(models.Model):
	userkey = models.TextField(max_length=10)
	original_filename = models.TextField()
	date = models.DateTimeField()
	sreads_file = models.FileField(null=True)
	user_email = models.EmailField(null=True)
	pre_path = models.TextField(null=True)
	SAM_path = models.TextField(null=True)
	post_path = models.TextField(null=True)
	VCF_path = models.TextField(null=True)

	def __str__(self):
		return self.name


class Pairedjob(models.Model):
	#randkey = models.TextField(max_length=10, primary_key=True)
	date = models.DateTimeField()

	def __str__(self):
		return self.name

'''class Single_outputs(models.Model):
	#key = models.ForeignKey(Single_job, on_delete=models.cascade)
	pre_path = models.TextField()
	SAM_path = models.TextField()
	post_path = models.TextField()
	VCF_path = models.TextField()

	def __str__(self):
		return self.name'''

class Paired_outputs(models.Model):
	#key = models.ForeignKey(Paired_job, on_delete=models.cascade)
	pre_path = models.TextField()
	SAM_path = models.TextField()
	post_path = models.TextField()
	VCF_path = models.TextField()

	def __str__(self):
		return self.name

class UploadFile(models.Model):
	title = models.CharField(max_length=50)
	file = models.FileField()




'''
class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField()
    uploaded_at = models.DateTimeField(auto_now_add=True)
'''