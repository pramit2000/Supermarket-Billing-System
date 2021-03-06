from django.shortcuts import render,redirect
from django.contrib import messages
# Create your views here.
import time
from .models import emp_login


def home(request):
    return render(request,'home.html')



def signup(request):
    if request.method == 'GET':
        return render(request,'signup.html')
    elif request.method == 'POST':
        time.sleep(30)
        messages.success(request, "User created Succesfully")
        return redirect('/signin')

def continueToSignup(request):
    if request.method == 'POST':
        return render(request,'verifyOTP.html')

def signin(request):
    if request.method == 'GET' :
     return render(request,'signin.html')
    elif request.method == 'POST':
       email = request.POST['empEmail']
       password = request.POST['empPassword']
       flag = checkLoginDetailsOfEmp(email,password)

    if flag:
        return render(request,'empDashboard.html')
    else:
        messages.error(request, 'error')
        return redirect('/signin/')

def logout(request):
    return redirect('/')

def checkLoginDetailsOfEmp(email,password):
    query = "SELECT id,email_id_id FROM user_emp_login where email_id_id = '"+email+"' and password = '"+password+"' LIMIT 1"
    try:
        email_id = (emp_login.objects.raw(query)[0]).email_id_id
    except:
        email_id=''
    if email_id == email:
       return True
    else:
       return False

