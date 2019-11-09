from django.shortcuts import render

from django.http import HttpResponse

def menu(request):
	return render(request, 'wrapper.html')

def home_page(request):
	return render(request, 'home.html')	

def registration(request):
	return render(request, 'registration.html')	