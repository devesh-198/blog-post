from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from . models import BlogPost
from . forms import BlogPostForm

# Create your views here.
def index(request) :
    """The home page for blog post"""
    blogs = BlogPost.objects.order_by('date_added')
    context = {'blogs' : blogs}
    return render(request, 'blogs/index.html', context)

@login_required
def new_blog(request) :
    """page to add new blog"""
    if request.method != 'POST' :
        # No data submited.
        form = BlogPostForm
    else :
        # Post data submitted, process data.
        form = BlogPostForm(data = request.POST)
        if form.is_valid() :
            new_blog = form.save(commit=False)
            new_blog.owner = request.user
            new_blog.save()
            return redirect('blogs:index')
    
    # Display a blank invalid form
    context = {'form' : form}
    return render(request, 'blogs/new_blog.html', context)

@login_required
def edit_blog(request, blog_id) :
    """page to edit a blog"""
    blog = BlogPost.objects.get(id=blog_id)
    if blog.owner != request.user :
        raise Http404

    if request.method != 'POST' :
        #initial request, pre-fill form with current entry.
        form = BlogPostForm(instance=blog)
    else :
        #POST data submitted, process data.
        form = BlogPostForm(instance=blog, data=request.POST)
        if form.is_valid() :
            form.save()
            return redirect('blogs:index')
    
    context = {'blog' : blog, 'form' : form}
    return render(request, 'blogs/edit_blog.html', context)
