from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.db import reset_queries

from align.models import *
from align.forms import *
from align.static.align.pyscripts.mitositefuncs import *

#pages in choose app

def index(request):
	return render(request, 'align/choose.html')

def paired(request):
	return render(request, 'align/paired.html')

def choose(request):
	return render(request, 'align/choose.html')

def loading(request):
	return render(request, 'align/loading.html')

def upload_single(request):
	return render(request, 'align/testredirect.html')

def results(request):
	return render(request, 'align/results.html')

#Pages in programmes app

def tutorial(request):
	return render(request, 'programmes/tutorial.html')

def about(request):
	return render(request, 'programmes/about.html')

def programmes(request):
	return render(request, 'programmes/programmes.html')

#Site processes

def handle_uploaded_file(f):
	key = getkey()
	dirpath = "/project/home17/whb17/public_html/django-framework/mitosite/align/media/uploads/" + key +"/"
	os.mkdir(dirpath)
	UPLOADED_FILE = dirpath + "userupload1.fastq"

	with open(UPLOADED_FILE, 'wb+') as destination:
		for chunk in f.chunks():
			destination.write(chunk)

	# open upload file for reading
	my_file = open(UPLOADED_FILE)

def uploadtest(request):
	upload_message = "Please upload reads in FASTQ format only."
	if request.method == 'POST':
		form = UploadFileForm(request.POST, request.FILES)
		if form.is_valid():
			handle_uploaded_file(request.FILES['file'])
			print(key)
			return render(request, 'align/loading.html', {'upload_message': "Uploaded file successfully", 'random_key': key })
		else:
			upload_message = "Not a valid file format"
	else:
		form = UploadFileForm()
		return render(request, 'align/simple_upload.html', {'upload_message': upload_message, 'form':form})

	'''upload_message = "Waiting for files."
	if request.method == 'POST':
		form = UploadFileForm
		if form.is_valid():
			form.save()
			return render(request, 'align/simple_upload.html', {'upload_message': "Uploaded file successfully", 'random_key' : randkey})
	else:
		form = UploadFileForm()
	return render(request, 'align/simple_upload.html', {'upload_message': "Please upload valid file format."})'''

'''def model_form_upload(request):
	if request.method == 'POST':
		form = DocumentForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('align/simple_upload.html')
	else:
		form = DocumentForm()
	return render(request, 'align/simple_upload.html', {
		'form': form
	})'''

def single(request):
	upload_message = "Please upload reads in FASTQ format only. This is seperate from the test upload."
	if request.method == 'POST':
		form = SinglejobForm(request.POST, request.FILES)
		if form.is_valid():
			handle_uploaded_file(request.FILES['sreads_file'])
			return render(request, 'align/single.html', {'upload_message': "Uploaded file successfully. This is seperate from the test upload.", 'random_key' : randkey})
		else:
			upload_message = "Not a valid file format"
	else:
		return render(request, 'align/single.html', {'upload_message': upload_message})

'''
def RetrieveJob(request):

'''