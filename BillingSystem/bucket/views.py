from django.shortcuts import render
from .models import products
total=0
# Create your views here.
def bucket(request):
    items=products.objects.all()
    total= request.POST['total']
    return render(request,'bucket.html',{"items":items})
    
    
def payment(request):
   # total=request.GET.get('total')
        return render(request,'payment.html',{"total":total})
    
    