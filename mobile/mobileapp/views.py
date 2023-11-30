from django.shortcuts import render
from . forms import Mobileform
from .models import Mobile

# Create your views here.

def index(request):
    context={}


    if request.method=='POST':
        if  'submit' in request.POST:
            print(request.POST)
            mobile_form=Mobileform(request.POST)
            mobile_form.save()

    mobile=Mobile.objects.all()
    mobile_form=Mobileform()
    context['mobile_form']=mobile_form
    context['mobile']=mobile



    return render (request,'index.html',context)