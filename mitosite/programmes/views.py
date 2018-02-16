from django.shortcuts import render

def index(request):
    return render(request, 'programmes/programmes.html')

#third parameter is a dictionary, this is optional parameter

def about(request):
    return render(request, 'programmes/about.html')

def tutorial(request):
    return render(request, 'programmes/tutorial.html')

