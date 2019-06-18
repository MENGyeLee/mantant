from django.shortcuts import render
from django.shortcuts import render,HttpResponse,HttpResponseRedirect,render_to_response
from django.template import Context,Template
from django.core.paginator import Paginator
from . import models
from showapp.models import movies
from showapp.models import shubao
from showapp.models import phones
from showapp.models import weathers

# Create your views here.
def main(request):
    return render(request,'main\\web.html') 
 

def db(request):
    douban=models.movies.objects.all()
    #return render(request,'main\web_db.html',{'content':douban}) 
    p = Paginator(douban,10)   
    if p.num_pages <= 1:  
        content_list = douban  
        data = ''  
    else:
        page = int(request.GET.get('page',1))  
        content_list = p.page(page) 
        left = []  
        right = []  
        left_has_more = False  
        right_has_more = False  
        first = False   
        last = False  
        total_pages = p.num_pages  
        page_range = p.page_range  
        if page == 1:  
            right = page_range[page:page+2]  
            print(total_pages)
            if right[-1] < total_pages - 1:    
                right_has_more = True
            if right[-1] < total_pages:   
                last = True
        elif page == total_pages:  
            left = page_range[(page-3) if (page-3) > 0 else 0:page-1]  
            if left[0] > 2:
                left_has_more = True  
            if left[0] > 1: 
                first = True
        else:  
            left = page_range[(page-3) if (page-3) > 0 else 0:page-1]   
            right = page_range[page:page+2] 
            if left[0] > 2:
                left_has_more = True
            if left[0] > 1:
                first = True
            if right[-1] < total_pages - 1:
                right_has_more = True
            if right[-1] < total_pages:
                last = True
        data = {    
            'left':left,
            'right':right,
            'left_has_more':left_has_more,
            'right_has_more':right_has_more,
            'first':first,
            'last':last,
            'total_pages':total_pages,
            'page':page
        }
    #return render_to_response("main\\db2.html",locals()) #必须用这个return 
    return render(request,'main\\web_db.html',context={'content_list':content_list,'data':data })
   
def tq(request):
    tianqi=models.weathers.objects.all()
    #return render(request,'main\web_tq.html',{'weathers':tianqi}) 
    p = Paginator(tianqi,10)   
    if p.num_pages <= 1:  
        content_list = tianqi  
        data = ''  
    else:
        page = int(request.GET.get('page',1))  
        content_list = p.page(page) 
        left = []  
        right = []  
        left_has_more = False  
        right_has_more = False  
        first = False   
        last = False  
        total_pages = p.num_pages  
        page_range = p.page_range  
        if page == 1:  
            right = page_range[page:page+2]  
            print(total_pages)
            if right[-1] < total_pages - 1:    
                right_has_more = True
            if right[-1] < total_pages:   
                last = True
        elif page == total_pages:  
            left = page_range[(page-3) if (page-3) > 0 else 0:page-1]  
            if left[0] > 2:
                left_has_more = True  
            if left[0] > 1: 
                first = True
        else:  
            left = page_range[(page-3) if (page-3) > 0 else 0:page-1]   
            right = page_range[page:page+2] 
            if left[0] > 2:
                left_has_more = True
            if left[0] > 1:
                first = True
            if right[-1] < total_pages - 1:
                right_has_more = True
            if right[-1] < total_pages:
                last = True
        data = {    
            'left':left,
            'right':right,
            'left_has_more':left_has_more,
            'right_has_more':right_has_more,
            'first':first,
            'last':last,
            'total_pages':total_pages,
            'page':page
        }
    #return render_to_response("main\\web_tq.html",locals()) #必须用这个return 
    return render(request,'main\\web_tq.html',context={'content_list':content_list,'data':data })

def jd(request):
    jingd=models.phones.objects.all()
    #return render(request,'main\web_jd.html',{'content':jingd}) 
    p = Paginator(jingd,10)   
    if p.num_pages <= 1:  
        content_list = jingd  
        data = ''  
    else:
        page = int(request.GET.get('page',1))  
        content_list = p.page(page) 
        left = []  
        right = []  
        left_has_more = False  
        right_has_more = False  
        first = False   
        last = False  
        total_pages = p.num_pages  
        page_range = p.page_range  
        if page == 1:  
            right = page_range[page:page+2]  
            print(total_pages)
            if right[-1] < total_pages - 1:    
                right_has_more = True
            if right[-1] < total_pages:   
                last = True
        elif page == total_pages:  
            left = page_range[(page-3) if (page-3) > 0 else 0:page-1]  
            if left[0] > 2:
                left_has_more = True  
            if left[0] > 1: 
                first = True
        else:  
            left = page_range[(page-3) if (page-3) > 0 else 0:page-1]   
            right = page_range[page:page+2] 
            if left[0] > 2:
                left_has_more = True
            if left[0] > 1:
                first = True
            if right[-1] < total_pages - 1:
                right_has_more = True
            if right[-1] < total_pages:
                last = True
        data = {    
            'left':left,
            'right':right,
            'left_has_more':left_has_more,
            'right_has_more':right_has_more,
            'first':first,
            'last':last,
            'total_pages':total_pages,
            'page':page
        }
    #return render_to_response("main\\web_jd.html",locals()) #必须用这个return  
    return render(request,'main\\web_jd.html',context={'content_list':content_list,'data':data })
    

def tb(request):
    taob=models.shubao.objects.all()
    #return render(request,'main\web_tb.html',{'shubao':taob})
    p = Paginator(taob,10)   

    if p.num_pages <= 1:  
        content_list = taob  
        data = ''  
    else:
        page = int(request.GET.get('page',1))  
        content_list = p.page(page) 
        left = []  
        right = []  
        left_has_more = False  
        right_has_more = False  
        first = False   
        last = False  
        total_pages = p.num_pages  
        page_range = p.page_range  
        if page == 1:  
            right = page_range[page:page+2]  
            print(total_pages)
            if right[-1] < total_pages - 1:    
                right_has_more = True
            if right[-1] < total_pages:   
                last = True
        elif page == total_pages:  
            left = page_range[(page-3) if (page-3) > 0 else 0:page-1]  
            if left[0] > 2:
                left_has_more = True  
            if left[0] > 1: 
                first = True
        else:  
            left = page_range[(page-3) if (page-3) > 0 else 0:page-1]   
            right = page_range[page:page+2] 
            if left[0] > 2:
                left_has_more = True
            if left[0] > 1:
                first = True
            if right[-1] < total_pages - 1:
                right_has_more = True
            if right[-1] < total_pages:
                last = True
        data = {    
            'left':left,
            'right':right,
            'left_has_more':left_has_more,
            'right_has_more':right_has_more,
            'first':first,
            'last':last,
            'total_pages':total_pages,
            'page':page
        }
    #return render_to_response("main\\web_tb.html",locals()) #必须用这个return   
    return render(request,'main\\web_tb.html',context={'content_list':content_list,'data':data })