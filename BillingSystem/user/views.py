from django.shortcuts import render,redirect
# Create your views here.
def home(request):
    return render(request,'home.html')

def signup(request):
    if request.method == 'GET':
        return render(request,'signup.html')
    elif request.method == 'POST':
        return redirect('/')

def signin(request):
    return render(request,'signin.html')

def checkUser(request):
    return render(request,'home.html')
