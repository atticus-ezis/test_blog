from django import forms 
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Blog, Comment

        
class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title','text_content']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text_content']