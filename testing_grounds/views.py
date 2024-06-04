from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog

# Create your views here.
def index(request):
    blogs = Blog.objects.all()
    context = {'blogs':blogs}
    return render(request, 'testing_grounds/index.html',context)
