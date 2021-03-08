from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'home.html')

def add(request):
    val1=int(request.POST['num1'])
    val2=int(request.POST['num2'])
    res=val1+val2
    return render(request,'result.html',{'result': res})

def minus(request):
    val1=int(request.POST['num1'])
    val2=int(request.POST['num2'])
    res=val1-val2
    return render(request,'result.html',{'result':res})

def multiply(request):
    val1=int(request.POST['num1'])
    val2=int(request.POST['num2'])
    res=val1*val2
    return render(request,'result.html',{'result':res})

def divide(request):
    val1=int(request.POST['num1'])
    val2=int(request.POST['num2'])
    res=val1/val2
    return render(request,'result.html',{'result':res})
