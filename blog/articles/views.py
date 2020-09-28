from django.shortcuts import render
from django.http import HttpResponse 
from django import template 
from .models import Article 

def archive(request):
	return render(request, 'templates/archive.html', 
		{"posts": Article.objects.all()})


