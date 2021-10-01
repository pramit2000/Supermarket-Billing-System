from django.shortcuts import render,redirect
# Create your views here.
def index(request):
    return render(request,'index.html')

def signup(request):
    if request.method == 'GET':
        return render(request,'signup.html')
    elif request.method == 'POST':
        return redirect('/')

