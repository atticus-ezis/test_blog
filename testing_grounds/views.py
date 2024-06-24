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

from .models import Blog, Comment, Folder
from .forms import BlogForm, CommentForm, FolderForm, AddBlogtoFolderForm

@login_required(login_url='login')
def profile(request):
    user = request.user
    folders = Folder.objects.filter(user=user)
    folder_form = FolderForm()
    add_blog_to_folder_form = AddBlogtoFolderForm()
    context = {'user':user, 'folder_form':folder_form, 'add_blog_to_folder_form':add_blog_to_folder_form, 'folders':folders}
    return render(request, 'testing_grounds/profile.html', context)

def get_profile_context(request, folder_form):
    user = request.user
    folders = Folder.objects.filter(user=user)
    add_blog_to_folder_form = AddBlogtoFolderForm(user=user)
    context = {
        'user': user,
        'folder_form': folder_form,
        'add_blog_to_folder_form': add_blog_to_folder_form,
        'folders': folders
    }
    return context


def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('index')
    if request.method=="POST":
        username = request.POST.get('username').lower()  
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
            user = form.save (commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'An error occured during registration')
    context = {'form':form}
    return render(request,'testing_grounds/login_register.html',context)

def index(request):
   blogs = Blog.objects.order_by('-pub_date')
   comment_form = CommentForm()
   context = {'blogs':blogs, 'comment_form':comment_form}
   return render(request, 'testing_grounds/index.html', context)
   

@login_required(login_url = 'login')
def form(request):
    if request.method == 'POST':
        content = BlogForm(request.POST)
        if content.is_valid():
            blog_post = content.save(commit=False)
            blog_post.user = request.user
            content.save()
            return HttpResponseRedirect((reverse('index')))
    else:
        content = BlogForm()
    return render(request, 'testing_grounds/submit_form.html', {'content':content})

@login_required(login_url = 'login')
def comment(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if request.method == 'POST':
        content = CommentForm(request.POST)
        if content.is_valid():
            comment_post = content.save(commit=False)
            comment_post.user = request.user
            comment_post.blog = blog
            content.save()
            return HttpResponseRedirect((reverse('index')))
    else:
        content = CommentForm()
    return render(request, 'testing_grounds/submit_form.html', {'content':content})

@login_required(login_url='login')
def delete(request, pk, model_name):
    if model_name == 'blog':
        blog = Blog.objects.get(id=pk)
    #if request.user != Blog.user
        #return HttpResponse('You're not the author')
        blog.delete()
        return HttpResponseRedirect((reverse('index')))
    if model_name == 'comment':
        comment = Comment.objects.get(id=pk)
        comment.delete()
        return HttpResponseRedirect((reverse('index')))

@login_required(login_url='login')
def edit(request, pk, model_name):
    if model_name == 'blog':
        selected_blog = get_object_or_404(Blog, pk=pk)
        if request.method == 'POST':
            form = BlogForm(request.POST, instance = selected_blog)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect((reverse('index')))
        else:
            content = BlogForm(instance=selected_blog)
        return render(request, 'testing_grounds/submit_form.html', {'content':content})

    elif model_name == 'comment':
        selected_comment = get_object_or_404(Comment, pk=pk)
        if request.method == 'POST':
            form = CommentForm(request.POST, instance = selected_comment)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect((reverse('index')))
        else:
            content = CommentForm(instance=selected_comment)
        return render(request, 'testing_grounds/submit_form.html', {'content':content})

@login_required(login_url='login')   
def like(request, pk, model_name):
    if model_name == 'blog':
        blog = get_object_or_404(Blog, pk=pk)
        blog.likes += 1
        blog.save()
        return HttpResponseRedirect(reverse('index'))
    else:
        model_name == 'comment'
        comment = get_object_or_404(Comment, pk=pk)
        comment.likes += 1
        comment.save()
        return HttpResponseRedirect(reverse('index'))

@login_required(login_url='login') 
def create_folder(request):
    if request.method == 'POST':
        form = FolderForm(request.POST)
        if form.is_valid():
            folder = form.save(commit=False)
            folder.user = request.user
            folder.save()
            return HttpResponseRedirect(reverse('profile'))
        else:
            form = FolderForm()
        context = get_profile_context(request, form)
        return render(request, 'testing_grounds/profile.html', context)


@login_required
def add_blog_to_folder(request):
    if request.method == 'POST':
        form = AddBlogtoFolderForm(request.POST, user=request.user)
        if form.is_valid():
            folder = form.cleaned_data['folder']
            blog = form.cleaned_data['blog']
            folder.blogs.add(blog)
            return redirect('folder_list')
    else:
        form = AddBlogtoFolderForm(user=request.user)
    return render(request, 'add_blog_to_folder.html', {'form': form})

@login_required
def folder_list(request):
    folders = Folder.objects.filter(user=request.user)
    return render(request, 'folder_list.html', {'folders': folders})
        
