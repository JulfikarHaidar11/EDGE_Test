from django.shortcuts import render

from django.views import View

from django.http import HttpResponse

def hello_django(View):
    return HttpResponse("Hello, Django!"),
