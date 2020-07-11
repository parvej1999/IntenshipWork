from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate

# Create your views here.


def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            newUser = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Congrats! your account is created successfully {username}')
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, newUser)
            return redirect('dashboard')

    else:
        form = UserCreationForm()

    context = {
        'form': form,
        'title': 'Sign Up'
    }
    return render(request, 'registration/signup.html', context)
