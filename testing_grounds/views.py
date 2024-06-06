from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, FormView
from django.urls import reverse, reverse_lazy
from .models import Blog
from .forms import BlogForm

class index(ListView):
   model = Blog
   template_name = 'testing_grounds/index.html'
   context_object_name = 'blogs'
   def get_queryset(self):
       return Blog.objects.all().order_by('-pub_date')

def form(request):
    if request.method == 'POST':
        content = BlogForm(request.POST)
        if content.is_valid():
            content.save()
            return HttpResponseRedirect((reverse('index')))
    else:
        content = BlogForm()
    return render(request, 'testing_grounds/submit_form.html', {'content':content})

def delete(request, pk):
    blog = Blog.objects.get(id=pk)
    blog.delete()
    return HttpResponseRedirect((reverse('index')))

def edit(request, pk):
    selected_blog = get_object_or_404(Blog, pk=pk)
    if request.method == 'POST':
        form = BlogForm(request.POST, instance = selected_blog)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect((reverse('index')))
    else:
        content = BlogForm(instance=selected_blog)
    return render(request, 'testing_grounds/submit_form.html', {'content':content})

    

