from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from blog.models import Post


class UserRegistration(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['email', 'username', 'first_name', 'last_name']


class UserUpdate(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']


class ProfileUpdate(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']


class AddPost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'category', 'image', 'post', 'author']


class UpdatePost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'category', 'image', 'post', 'author']
