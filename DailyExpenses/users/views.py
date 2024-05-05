from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, LoginForm, ProfileUpdateForm
from django.contrib.auth import login, authenticate



def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        for field in form:
            print("Field Error:", field.name, field.data)
        if form.is_valid():
            form.save()
            #username = form.cleaned_data.get('username')
            messages.success(request, 'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        messages.error(request, "Invalid username or password.")
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required(login_url='/login')
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)


def login_user(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        for field in form:
            print("Field Error:", field.name, field.data)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("/home")
            else:
                messages.error(request, "Invalid username or password....")
        else:
            messages.error(request, "Invalid username or password.123")
    else:
        form = LoginForm()
    context = {
        'form': form,
    }

    return render(request, 'users/login.html', context)
