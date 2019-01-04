from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
# help page in the template folder
#    return HttpResponse("Toolingstrat view!")
    toolingstrat_dict = {
        'bodytoolingstrat':"Hello the message is now coming from view.py for TOOLINGSTRAT"
    }
    return render(request,'toolingstrat/index.html',context=toolingstrat_dict)
