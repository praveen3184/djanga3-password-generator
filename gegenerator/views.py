from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def home(request):
    return render(request,'gegenerator/home.html')

def aboutus(request):
    return render(request,'gegenerator/aboutus.html')

def password(request):

    characters = list ('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        characters.extend(list ('ABCDEFGHIJKLMNOPQRSTUVWXZ'))

    if request.GET.get('special'):
        characters.extend(list ('!@#$%^&*'))

    if request.GET.get('numbers'):
        characters.extend(list ('1234567890'))

    length = int (request.GET.get('length'))
    thepassword = ''

    for x in range(length):
        thepassword += random.choice(characters)
    return render(request,'gegenerator/password.html',{'password':thepassword})
