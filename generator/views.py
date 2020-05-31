from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import random

def home(request):
    return render(request,'generator/home.html',{'password': 'dwefwgw'})

def about(request):
    return render(request,'generator/about.html')


def password(request):
    thepassword = 'testing'


    characters = list('abcdefghijklmnopqrstuvwxyz')
    length = int(request.GET.get('length',12))

    if request.GET.get('uppercase'):
        characters.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    if request.GET.get('special'):
        characters.extend('!@#$%^&*()')

    if request.GET.get('numbers'):
        characters.extend('1234567890')

    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)


    return render(request, "generator/password.html", {'password':thepassword})