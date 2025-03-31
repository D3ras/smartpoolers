from django.contrib import messages
from django.http.response import HttpResponseRedirect
from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

class Login(View):
    def get(self, request):
        current_user = request.user
        if current_user.id:
            messages.success(request, 'Already logged in!!!')
            return redirect('ShopHome')
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('ShopHome')
        else:
            messages.warning(request, "E-mail or Password Incorrect!!!")
            return render(request, 'login.html', {'email':email})