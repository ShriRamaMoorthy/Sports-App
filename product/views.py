from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
def base_view(request,*args,**kwargs):
    #print(args,kwargs)
    #print(request.user)
    #return HttpResponse("<h1>Hello World!!!</h1>")
    return render(request,"base.html",{})

def home_view(request,*args,**kwargs):
    #print(args,kwargs)
    #print(request.user)
    #return HttpResponse("<h1>Hello World!!!</h1>")
    return render(request,"home1.html",{})

def contact_view(request,*args,**kwargs):
    #print(args,kwargs)
    #print(request)
    mycontext={
        "mytest":'this is about django',
        "mynumber":123,
        'mylist':[456,589,'abc','CR7!!!'],
        'html':"<h2>just a tag</h2>"
    }
    return render(request,"contact.html",mycontext)

def product_detail_view(request):
    return render(request,"",{})