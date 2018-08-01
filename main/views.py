from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse, Http404, HttpResponseForbidden, HttpResponseNotAllowed
from django.contrib.auth import logout, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views import View
from .backend import authenticate
from .forms import SignUpForm, ProfileForm



def signup(request):
    if request.method == 'POST':
        signup_form = SignUpForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()
            profile_form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        signup_form = SignUpForm()
        profile_form = ProfileForm()
    return render(request, 'main/signup.html', {
        'signup_form': signup_form,
        'profile_form': profile_form,
        })

@login_required
def index(request):
    return render(request, 'main/landing.html')

class LoginView(View):

    def get(self, request, *args, **kwags):
        if request.user.is_authenticated:
            return redirect('/')
        return render(request, 'main/login.html')

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(
                request, 'Failed to sign in! Please check your name and PIN', extra_tags='danger')
            return redirect('/login')

@login_required
def logout_view(request):
    logout(request)
    return redirect('/login')

@login_required
def about(request):
   return render(request, 'main/about.html')

@login_required
def workout(request):
   return render(request, 'main/workout.html')

@login_required
def feed(request):
   return render(request, 'main/feed.html')