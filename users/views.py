from django.shortcuts import render,redirect,reverse
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from . import forms
import os
import requests
from . import models
from django.contrib.auth import authenticate,login,logout
# Create your views here.
class LoginView(FormView):

    def get(self,request):
        form = forms.LoginForm()
        return render(request,"users/login.html",{"form":form})

    def post(self,request):
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user=authenticate(self,request,username=email,password=password)
            if user is not None:
                login(self.request,user)
                redirect(reverse("core:home"))
        return render(request,"users/login.html",{"form":form})

def log_out(request):
    logout(request)
    return redirect(reverse("core:home"))


class SignUpView(FormView):
    template_name="users/signup.html"
    form_class=forms.SignUpForm
    success_url=reverse_lazy("core:home")
    def form_valid(self, form):
        form.save() 
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user=authenticate(self.request,username=email,password=password)
        if user is not None:
            login(self.request,user)
        user.verify_email()
        return super().form_valid(form)

def complete_verification(request, key):
    try:
        user = models.User.objects.get(email_secret=key)
        user.email_verified = True
        user.email_secret = ""
        user.save()
        # to do: add succes message
    except models.User.DoesNotExist:
        # to do: add error message
        pass
    return redirect(reverse("core:home"))

def github_login(request):
    client_id=os.environ.get("GH_ID")
    print(client_id)
    redirect_uri='http://127.0.0.1:8000/users/login/github/callback'
    return redirect(f"https://github.com/login/oauth/authorize?client_id={client_id}&redirect_uri={redirect_uri}&scope=read:user")

def github_callback(request):
    code = request.GET.get("code",None)
    if code is not None:
        pass
    