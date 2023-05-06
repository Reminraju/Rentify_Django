from django.shortcuts import render,redirect
from .models import reg,log,head,con,boo
from django.http import JsonResponse
from django.contrib import messages
# Create your views here.
def geg(request):
    return  render(request,"frontpage.html")
def ger(request):   
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['psw']
        repassword=request.POST['psw-repeat']
        emailexist=reg.objects.filter(email=email)
        if emailexist:
            messages.info(request,"email already exist")
            return render(request,"register.html")
        elif password!=repassword:
            messages.info(request,"password doesn't match")
            return render(request,"register.html")
        else:
            reg(email=email,password=password,confirmpassword=repassword).save()
            return redirect("log")
    return render(request,"register.html")
def ter(request):
    return render(request,"terms.html")
def log(request):
     if request.method=='POST':
        try:
            Userdetails=reg.objects.get(email=request.POST['email'],password=request.POST['psw'])
            request.session['email']=Userdetails.email
            return redirect('hed')
        except reg.DoesNotExist as e:
            messages.success(request,'username' or 'password invalid')
     return render(request,"login.html")
def contact(request):
    if request.method=='POST':
        name=request.POST['name']
        country=request.POST['country']
        subject=request.POST['subject']
        con(name=name,country=country,subject=subject).save()
        messages.success(request,'the new user'+request.POST['name']+" is saved successfully...!")  
    return render(request,"contact.html")
def abo(request):
    return render(request,"aboutus.html")
def hed(request):
    a = head.objects.all()
    context = {
        'a' : a
    }
    return render(request,"main.html",context)
def book(request):
    if request.method=='POST':
        Address=request.POST['Address']
        number=request.POST['number']
        boo(Address=Address,number=number).save()

    return render(request,"booking.html")
    