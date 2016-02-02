from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views.generic import View

def index(request):
  return HttpResponse("Hello, world")
