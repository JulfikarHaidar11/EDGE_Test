from django.shortcuts import render

from django.views import View
from django.http import HttpResponse

class MyView(View):
    def get(self , request):
        return HttpResponse("Wellcome to Django from class view"),
