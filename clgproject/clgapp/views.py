from django.contrib import messages,auth
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
# Create your views here.

def home(request):
    return render(request,'home.html')
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return render(request,'newpage.html')
        else:
            messages.info(request,"invalid")
            return redirect('login')
    return render(request,'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirmpassword = request.POST['confirmpassword']

        # name = request.POST['name']
        # dob = request.POST['dob']
        # age = request.POST['age']
        # gender = request.POST['gender']
        # phonenumber = request.POST['phonenumber']
        # mailid = request.POST['maildid']
        # address = request.POST['address']
        # department = request.POST['department']
        # course = request.POST['course']
        # purpose = request.POST['purpose']
        # materialprovides = request.POST['materialprovides']

        if password==confirmpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"User already taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password)

                user.save();
                return redirect('login')

        else:
            messages.info(request,"password is not match")
            return redirect('register')
        return redirect('/')



    return render(request,"register.html")

def newpage(request):
    if request.method == 'POST':
        name = request.POST['name']
        dob = request.POST['dob']
        age = request.POST['age']
        gender = request.POST['gender']
        phonenumber = request.POST['phonenumber']
        mailid = request.POST['maildid']
        address = request.POST['address']
        department = request.POST['department']
        course = request.POST['course']
        purpose = request.POST['purpose']
        materialprovides = request.POST['materialprovides']

        if User.objects.filter(name=name).exists():
            messages.info(request,"User already taken")
            return redirect('register')
        else:
            user = User.objects.create_user(name=username,dob=dob,age=age,gender=gender,phonenumber=phonenumber,mailid=mailid,address=address,department=department,course=course,purpose=purpose,materialprovides=materialprovides)

            user.save();
            messages.info(request,"order confirmed")



    return render(request,'newpage.html')
def logout(request):
    auth.logout(request)
    return render(request,'home.html')

