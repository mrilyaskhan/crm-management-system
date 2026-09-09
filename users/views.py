from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect


def login_view(request):

    if request.user.is_authenticated:

        if request.user.groups.filter(name='Admin').exists():
            return redirect('dashboard')

        elif request.user.groups.filter(name='Sales').exists():
            return redirect('leads')

        return redirect('profile')

    form = AuthenticationForm(
        request,
        data=request.POST or None
    )

    if request.method == 'POST':

        if form.is_valid():

            user = form.get_user()

            login(request, user)

            if user.groups.filter(name='Admin').exists():
                return redirect('dashboard')

            elif user.groups.filter(name='Sales').exists():
                return redirect('leads')

            return redirect('profile')

    return render(
        request,
        'registration/login.html',
        {'form': form}
    )