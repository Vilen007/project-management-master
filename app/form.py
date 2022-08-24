from django import forms
from .models import *


# BookCreate
class ProjectCreate(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'

        widgets = {
            # 'userId': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.Select(attrs={'class': 'form-control'}),
            'created_at': forms.TextInput(attrs={'class': 'form-control'}),
            'end_date': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }


# TaskCreate
class TaskCreate(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'created_at', 'end_date', 'type', 'state', 'description']
        widgets = {
            # 'userId': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.Select(attrs={'class': 'form-control'}),
            'type': forms.Select(attrs={'class': 'form-control'}),
            'created_at': forms.TextInput(attrs={'class': 'form-control'}),
            'end_date': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }


# info create
class InfoCreate(forms.ModelForm):
    class Meta:
        model = Info
        fields = '__all__'

class CommentForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'md-textarea form-control',
        'placeholder': 'Comment here ...',
        'rows': '4',
    }))

    class Meta:
        model = Comment
        fields = ('body',)