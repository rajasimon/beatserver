from django.shortcuts import render
from django.http import HttpResponse
from channels import Channel

from random import randint
# Create your views here.
def home(request):
    number =  randint(1, 343333333)
    Channel('hae-repeat-me').send({'number': number, 'status': True})
    return HttpResponse("testing")
