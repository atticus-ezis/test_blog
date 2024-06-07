from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, FormView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

from .models import Blog
from .forms import BlogForm 

def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('index')
    if request.method=="POST":
        username = request.POST.get('username')  
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "User does not exist")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, "Username or password does not exist")

    context = {'page':page}
    return render(request, 'testing_grounds/login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('index')

def registerUser(request):
    form = UserCreationForm()
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form#.save (commit=False)
            #user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occured during registration')
    context = {'form':form}
    return render(request,'testing_grounds/login_register.html',context)

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

@login_required(login_url='login')
def delete(request, pk):
    blog = Blog.objects.get(id=pk)
    #if request.user != Blog.host
        #return HttpResponse('You're not the author')
    blog.delete()
    return HttpResponseRedirect((reverse('index')))

@login_required(login_url='login')
def edit(request, pk):
    selected_blog = get_object_or_404(Blog, pk=pk)
    #if request.user != Blog.host
        #return HttpResponse('You're not the author')
    if request.method == 'POST':
        form = BlogForm(request.POST, instance = selected_blog)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect((reverse('index')))
    else:
        content = BlogForm(instance=selected_blog)
    return render(request, 'testing_grounds/submit_form.html', {'content':content})

