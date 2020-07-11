from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Congrats! your account is created successfully {username}')
            return redirect('login')

    else:
        form = UserCreationForm()

    context = {
        'form': form,
        'title': 'Sign Up'
    }
    return render(request, 'registration/signup.html', context)
