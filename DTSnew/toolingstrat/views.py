from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
# help page in the template folder
    return HttpResponse("Toolingstrat view!")
