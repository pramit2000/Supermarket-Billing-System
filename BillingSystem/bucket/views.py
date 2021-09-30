from django.shortcuts import render
from .models import products
# Create your views here.
def index(request):
    items=products.objects.all()
    return render(request,'index.html',{"items":items})