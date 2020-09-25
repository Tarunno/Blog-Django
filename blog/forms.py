from django import forms
from django.utils import timezone
from django.contrib.auth.models import User
from .models import Comment


class AddComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['post', 'user', 'text']
