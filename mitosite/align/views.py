from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.db import reset_queries

from align.models import *
from align.forms import *
import align.static.align.pyscripts.mitositefuncs as msf
import align.static.align.pyscripts.emailstart as smail
import os
import sys
import smtplib
from email.mime.text import MIMEText as text



#pages in choose app

def index(request):
	return render(request, 'align/choose.html')

def single(request):
	return render(request, 'align/single.html')

def paired(request):
	return render(request, 'align/paired.html')

def choose(request):
	return render(request, 'align/choose.html')

def loading(request):
	return render(request, 'align/loading.html')

def results(request):
	return render(request, 'align/results.html')

def tutorial(request):
	return render(request, 'align/tutorial.html')

def about(request):
	return render(request, 'align/about.html')

def programmes(request):
	return render(request, 'align/programmes.html')

#Site processes

key = msf.keygen() # generate key
uploadpath = "/project/home17/whb17/public_html/django-framework/mitosite/align/media/uploads/" #upload path 

def handle_uploaded_single_file(f):
	key = msf.keygen()
	dirpath = "/project/home17/whb17/public_html/django-framework/mitosite/align/media/uploads/" + key +"/"
	os.mkdir(dirpath)
	UPLOADED_FILE = dirpath + "userupload1.fastq"

	with open(UPLOADED_FILE, 'wb+') as destination:
		for chunk in f.chunks():
			destination.write(chunk)

	# open upload file for reading
	my_file = open(UPLOADED_FILE)


def handle_uploaded_paired_file(f):
	
	UploadFile().randkey = key
	dirpath = uploadpath + key +"/"
	os.mkdir(dirpath)
	UPLOADED_FILE_1 = dirpath + "userupload1.fastq"
	UPLOADED_FILE_2 = dirpath + "userupload1.fastq"

	with open(UPLOADED_FILE_1, 'wb+') as destination:
		for chunk in f.chunks():
			destination.write(chunk)

	with open(UPLOADED_FILE_2, 'wb+') as destination:
		for chunk in f.chunks():
			destination.write(chunk)

	# open upload file for reading
	my_file_1 = open(UPLOADED_FILE_2)
	my_file_2 = open(UPLOADED_FILE_2)
	
	return key


def uploadtest(request):
	upload_message = "Please upload reads in FASTQ format only."
	if request.method == 'POST':
		form = UploadFileForm(request.POST, request.FILES)
		if form.is_valid():
			handle_uploaded_single_file(request.FILES['file'])

			# Set off job start alert
			user_email = form.cleaned_data['user_email']
			smail.startalert(user_email, key)

			#Transition to job start page displaying user key
			print(key)
			return render(request, 'align/loading.html', {'upload_message': "Uploaded file successfully", 'random_key': key })
		else:
			upload_message = "Not a valid file format"
	else:
		form = UploadFileForm()
		return render(request, 'align/simple_upload.html', {'upload_message': upload_message, 'form':form})


def SingleJob(request):
	upload_message = "Please upload reads in FASTQ format only."
	if request.method == 'POST':
		form = SingleJobForm(request.POST, request.FILES)
		if form.is_valid():
			handle_uploaded_single_file(request.FILES['readsfile'])
			print(key)
			return render(request, 'align/loading.html', {'upload_message': "Uploaded file successfully", 'random_key': key })
		else:
			upload_message = "Not a valid file format"
	else:
		form = SingleJobForm()
		return render(request, 'align/single.html', {'upload_message': upload_message, 'form':form})


def PairedJob(request):
	upload_message = "Please upload reads in FASTQ format only."
	if request.method == 'POST':
		form = PairedJobForm(request.POST, request.FILES)
		if form.is_valid():
			handle_uploaded_paired_file(request.FILES['readsfile1', 'readsfile2', 'adapters'])
			print(key)
			return render(request, 'align/loading.html', {'upload_message': "Uploaded file successfully", 'random_key': key })
		else:
			upload_message = "Not a valid file format"
	else:
		form = PairedJobForm()
		return render(request, 'align/paired.html', {'upload_message': upload_message, 'form':form})




	
'''
def RetrieveJob(request):

'''