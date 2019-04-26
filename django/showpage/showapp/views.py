from django.shortcuts import render
from django.shortcuts import render,HttpResponse
from django.template import Context,Template
from . import models
# Create your views here.
def main(request):
    return render(request,'main\web.html') 
 

def db(request):
    douban=models.movie.objects.get()
    return render(request,'main\web_db.html',{'content':douban})  
   
def tq(request):
    tianqi=models.movie.objects.get()
    return render(request,'main\web_tq.html',{'weather':tianqi}) 
    
def jd(request):
    jingd=models.movie.objects.get()
    return render(request,'main\web_jd.html',{'content':jingd})  

def tb(request):
    taob=models.movie.objects.get()
    return render(request,'main\web_tb.html',{'shubao':taob})  