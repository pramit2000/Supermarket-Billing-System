from django.shortcuts import render
from .models import products
# Create your views here.
def bucket(request):
    items=products.objects.all()
    return render(request,'bucket.html',{"items":items})