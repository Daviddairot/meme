from django import forms
from .models import BlogPost
from .models import UserProfile
from django.contrib.auth.models import User


from django import forms
from .models import BlogPost

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'image', 'video']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your blog content'}),
            'image': forms.FileInput(attrs={'class': 'form-control-file'}),
            'video': forms.FileInput(attrs={'class': 'form-control-file'}),
        }


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_pic', 'bio']

        widgets = {
            'profile_pic': forms.FileInput(attrs={'class': 'form-control-file'}),
            'bio': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Tell something about yourself...'}),
        }
