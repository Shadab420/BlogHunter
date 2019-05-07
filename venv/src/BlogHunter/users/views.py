from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required

def register(request):

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username}! Your account has been created. You can now login')
            return redirect('user-login')
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', { 'useRegForm': form })

@login_required
def profile(request):
    if request.method == 'POST':
        userUpdateForm = UserUpdateForm(request.POST, instance = request.user)
        profileUpdateForm = ProfileUpdateForm(request.POST, request.FILES, instance = request.user.profile)

        if userUpdateForm.is_valid() and profileUpdateForm.is_valid():
            userUpdateForm.save()
            profileUpdateForm.save()
            messages.success(request, f'Your profile has been updated.')
            return redirect('user-profile')
    else:
        userUpdateForm = UserUpdateForm(instance=request.user)
        profileUpdateForm = ProfileUpdateForm(instance=request.user.profile)
    context = {

        'userUpdateForm' : userUpdateForm ,
        'profileUpdateForm' : profileUpdateForm
    }


    return render(request, 'users/profile.html', context)