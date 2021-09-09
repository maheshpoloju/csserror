from django.shortcuts import render
from modelPracticeApp.models import *

# Create your views here.
def index(request):
    return render(request,'index.html')

def hydjobs1(request):
    jobs_list=hydjobs.objects.order_by('date')
    my_dict={'jobs_list':jobs_list}
    return render(request,'hydjobs.html',context=my_dict)

def blorejobs(request):
    return render(request,'blorejobs.html')

def punejobs(request):
    return render(request,'apppunejobs.html')

def chennaijobs(request):
    return render(request,'chennaijobs.html')
