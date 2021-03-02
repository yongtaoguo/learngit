from django.shortcuts import render,HttpResponse
from gytest import models
# Create your views here.
def hello(request):
    return HttpResponse('hello')
