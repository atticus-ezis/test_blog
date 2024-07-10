from django import forms 
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Blog, Comment, Folder

        
class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title','text_content']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text_content']
        widgets = {
            'text_content': forms.Textarea(attrs={
                'cols': 40,  # Customize the width here
                'rows': 1,   # Customize the height here
            }),
        }
        labels = {
            'text_content': '',  # Remove the label text
        }

class FolderForm(forms.ModelForm):
    class Meta:
        model = Folder
        fields = ['name']

class AddBlogtoFolderForm(forms.Form):
    folder = forms.ModelChoiceField(queryset=Folder.objects.none())
    blog = forms.ModelChoiceField(queryset=Blog.objects.all())

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['folder'].queryset = Folder.objects.filter(user=user)

