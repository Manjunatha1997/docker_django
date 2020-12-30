from django.shortcuts import render
import os
from . server import *
import socket
import threading
from django.http import HttpResponse

# Create your views here.


def video(request):
    return render(request,'index.html')
    # return HttpResponse("hello..")

def run(request):
    os.system('python3 /home/manju/docker_django/record/app/recorder.py')
    return HttpResponse('recorder')
def run1(request):
    os.system('python3 /home/manju/docker_django/record/app/server.py')
    return HttpResponse('server')


