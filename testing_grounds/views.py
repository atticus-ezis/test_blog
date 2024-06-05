from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Blog
from .forms import BlogForm

def index(request):
    blogs = Blog.objects.all()
    context = {'blogs':blogs}
    return render(request, 'testing_grounds/index.html',context)

def form(request):
    if request.method == 'POST':
        content = BlogForm(request.POST)
        if content.is_valid():
            content.save()
            return redirect('success')
    else:
        content = BlogForm()
    return render(request, 'submit_form.html', {'content':content})

