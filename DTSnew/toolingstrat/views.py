from django.shortcuts import render
from django.http import HttpResponse
from . import form1
from toolingstrat.models import AppType, Region, Application

# Create your views here.

def index(request):
# help page in the template folder
#    return HttpResponse("Toolingstrat view!")
    toolingstrat_dict = {
        'bodytoolingstrat':"Hello the message is now coming from view.py for TOOLINGSTRAT"
    }
    return render(request,'toolingstrat/index.html',context=toolingstrat_dict)

def applist(request):

    application_list = Application.objects.order_by('app_name')
    app_dictionary = {'app_list':application_list}
    return render(request,'toolingstrat/applist.html',context=app_dictionary)

def forms(request):
    form = form1.FormOne()

    if request.method == 'POST':
        form = form1.FormOne(request.POST)

        if form.is_valid():
            print("validation succesful!")
            print("app name: " + form.cleaned_data['app_name'])
            print("app type: " + form.cleaned_data['app_type'])
            print("app id: " + form.cleaned_data['app_id'])


    return render(request, 'toolingstrat/form1.html', {'form':form})





    
