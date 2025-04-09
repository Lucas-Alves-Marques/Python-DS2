from django.shortcuts import render
from django.http import HttpResponse

def hello_world(request):
    
    return HttpResponse("Hello, World!")

def testMesage(request):
    return HttpResponse("Nova mensagem de teste!")