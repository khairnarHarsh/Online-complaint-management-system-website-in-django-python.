import json 
from pyexpat.errors import messages 
from django.contrib import messages 
from django.shortcuts import render ,HttpResponse,redirect 
from django.contrib.auth.models import * 
from django.contrib.auth import * 
from django.http import HttpResponse 
 
from django.template.loader import get_template 
 
from xhtml2pdf import pisa 
 
from .models import *

# from django.template import Context
# from django.http import HttpResponse


# from .filters import OrderFilter

# Create your views here.

def home(request):
    return render(request,'home.html')

def login1(request): 
   
             
    return render(request,'login1.html')
    
def logoutuser(request):
    logout(request)
    messages.success(request,"Logout Sucessfully")
    return redirect('home')

def studentlog(request):
    if request.method == "POST": 
        username = request.POST['username'] 
        password = request.POST['pass'] 
        user = authenticate(username=username, password=password) 
        if user: 
            login(request,user) 
            messages.success(request, "User login successfully") 
            # messages.pop(request, "User login successfully") 
            return redirect('home') 
        else: 
            messages.success(request,"Invalid Credentials") 
            return redirect('login1') 
           
    return render(request,'studentlog.html')


def adminlog(request):
    return render(request,'adminlog.html')

def regist(request):
    if request.method =="POST":
        username=request.POST["username"]
        fullname=request.POST["fullname"]
        email=request.POST["email"]
        password1=request.POST["password1"]
        password2=request.POST["password2"]
        if password1!=password2:
            return HttpResponse("your password and confirm password are not same!!")
        else:
            mobile=request.POST["mobile"]
            gender=request.POST["gender"]
            user=User.objects.create_user(username=username,email=email,password=password1)
            Userprofile.objects.create(user=user,mobile=mobile,password2=password2,fullname=fullname)
            user.save()
       
    return render(request,'regist.html',locals())
    

def profile(request):

    try:
        user= User.objects.get(id=request.user.id)
        data=Userprofile.objects.get(user=user)
    except Userprofile.DoesNotExist:
        data=None
    
    return render(request,'profile.html',locals())

def addcom(request):
    if request.method == "POST":
        
        user = User.objects.get(id=request.user.id)

       
        Type_of_complaint=request.POST['complaint']
        subject=request.POST['subject']
        Description = request.POST['Description']
        allComplaint.objects.create(user=user,Subject=subject,Type_of_complaint=Type_of_complaint,Description=Description)
        messages.success(request, "Complaint added Succesfully") 
        return render(request,'profile.html')
    
    return render(request,'addcom.html' ,locals())
    
def allcom(request):
    all1 = allComplaint.objects.all()
 
    return render(request,'allcom.html',locals())

def solvedcom(request):
    orderstatus =2

    data = allComplaint.objects.filter(status=orderstatus)

    return render(request,'solvedcom.html',locals())

def editpage(request):
    return render(request,'editpage.html')
def unsolvedcom(request):
    orderstatus =3
    data = allComplaint.objects.filter(status=orderstatus)
    return render(request,'unsolvedcom.html',locals())


def help(request):
    return render(request,'help.html')

def about(request):
    return render(request,'about.html')

def admin_dash(request):
    return render(request,'admin_dash.html')

def mycom(request):
    try:
        user = User.objects.get(id=request.user.id)
        data = allComplaint.objects.filter(user=user)
    except allComplaint.DoesNotExist:
        data=None 

    return render(request,'mycom.html',locals())

def pdf_report_create(request,pid): 
    # user = User.objects.get(id=request.user.id)
    # order = Booking.objects.filter(user=request.user) 
    # data = allComplaint.objects.get(id=pid)
    user = User.objects.get(id=request.user.id)
    data = allComplaint.objects.filter(id=pid)

 
    template_path = 'invoice.html' 
 
    context = {'data':data} 
    # 
 
    response = HttpResponse(content_type='application/pdf') 
 
    response['Content-Disposition'] = 'filename="products_report.pdf"' 
 
    template = get_template(template_path)
 
    html = template.render(context) 

    
 
    # create a pdf 
    pisa_status = pisa.CreatePDF( 
       html, dest=response) 
    # if error then show some funy view 
    if pisa_status.err: 
       return HttpResponse('We had some errors <pre>' + html + '</pre>') 
    return response

    

def delete(request,pid):
    # all1 = allComplaint.objects.get(user=request.user)
    instance = allComplaint.objects.filter(id=pid)
    instance.delete()
    return render(request,'mycom.html',locals())