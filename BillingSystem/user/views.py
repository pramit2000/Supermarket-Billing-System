from django.shortcuts import render,redirect

# Create your views here.
from .models import emp_login


def home(request):
    return render(request,'home.html')

def signup(request):
    if request.method == 'GET':
        return render(request,'signup.html')
    elif request.method == 'POST':
        return redirect('/')

def signin(request):
    if request.method == 'GET' :
     return render(request,'signin.html')
    elif request.method == 'POST':
       email = request.POST.get('empEmail')
       password = request.POST.get('empPassword')
       flag = checkLoginDetailsOfEmp(email,password)

       if flag:
           return render(request,'empDashboard.html')
       else:
           return redirect('/signin/')

def checkLoginDetailsOfEmp(email,password):
    query = 'select email_id from user_emp_login where email_id = %s and password = %s',[email],[password]
    email_id = emp_login.objects.raw(query)
    if email_id == email:
        return True
    else:
        return False