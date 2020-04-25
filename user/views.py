from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def register(request) :
    """Regiser  new user"""
    if request.method != 'POST' :
        # Display blank registration form.
        form = UserCreationForm
    else :
        #process completed form.
        form = UserCreationForm(data=request.POST)
        
        if form.is_valid() :
            new_user = form.save()
            # Log the user in and then redirect to home page.
            login(request, new_user)
            return redirect('blogs:index')

    # Display a blank or in valid form.
    context = {'form' : form}
    return render(request, 'registration/register.html', context)
        