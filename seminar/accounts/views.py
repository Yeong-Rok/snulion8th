from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.contrib.auth import logout as django_logout

# Create your views here.
def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
            auth.login(request, user)
            return redirect('/feeds/')
    return render(request, 'accounts/signup.html')


# def login(request):
#     if request.method == 'POST':
#         user = authenticate(username=request.POST['username'], password=request.POST['password'])
#         if user is not None:             
#             auth.login(request, user) #로그인을 시켜줌
#             return redirect('/feeds/')
#     return render(request, 'accounts/login.html')

# def logout(request):
#     django_logout(request)
#     return redirect('/feeds/')