from django import forms 

from . models import BlogPost

class BlogPostForm(forms.ModelForm) :
    """Form to make new blog post."""
    class Meta :
        model = BlogPost
        fields = ['title', 'text']
        lables = {'title' : 'Title'}
        lables = {'text' : 'Text'}

