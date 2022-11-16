from django.shortcuts import render
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import BlogForm
from .models import Blog
from django.core.mail import send_mail


def base(request):
    return render(request, 'base.html')


def home(request):
    blogs = Blog.objects.all()
    return render(request, 'home.html', {'blogs': blogs})


def contact(request):
    return render(request, 'contact.html')


def user_signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'User registered successfully')
            send_mail(
                      'Subject: presenting the email',
                      'message:new signup added successfully',
                      'ravindrareddy72868@gmail.com',
                      ['ravindrareddy72868@gmail.com'],
                      fail_silently=False
                      )
            print('mail sended')
        return render(request, 'signup.html', {'form': form})
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                passwd = form.cleaned_data['password']
                user = authenticate(username=username, password=passwd)
                if user is not None:
                    login(request, user)
                    print(user)
            return HttpResponseRedirect('/')
        else:
            form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})
    else:
        return HttpResponseRedirect('/')


def user_logout(request):
    if request.method == 'POST':
        logout(request)
        return HttpResponseRedirect('/')
    return render(request, 'logout.html')


@login_required(login_url='/login')
def add_blog(request):
    if request.method == 'POST':
        print(request.POST)
        form = BlogForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['Title']
            opinion = form.cleaned_data['Opinion']
            form = Blog(Created_by=request.user, Title=title, Opinion=opinion)
            form.save()
        return HttpResponseRedirect('hom')
    else:
        form = BlogForm()
    return render(request, 'blog.html', {'form': form})


def delete_blog(request, id):
    record = Blog.objects.get(pk=id)
    record.delete()
    return HttpResponseRedirect('/hom')


def delete_blog_dash(request, id):
    record = Blog.objects.get(pk=id)
    record.delete()
    return HttpResponseRedirect('/dashboard')


def edit_blog(request, id):
    record = Blog.objects.get(pk=id)
    form = BlogForm(instance=record)
    if request.method == 'POST':
        form = BlogForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/hom')
    else:
        return render(request, 'edit_blog.html', {'form': form})


def dashboard(request):
    blogs = Blog.objects.all()
    return render(request, 'dashboard.html', {'blogs': blogs})


def cookie(request):
    response = render(request, 'setcookie.html')
    response.set_cookie('name', 'alex', max_age=200)
    return response


def getcookie(request):
    name = request.COOKIES.get('name')
    return render(request, 'getcookie.html', {'name': name})


def delcookie(request):
    response = render(request, 'delcookie.html')
    response.delete_cookie('name')
    return response


def setsession(request):
    request.session['name'] = 'reddy'
    request.session['lname'] = 'ravi'
    request.session.set_expiry(10)
    return render(request, 'setsession.html')


def getsession(request):
    name = request.session.get('name')
    return render(request, 'getsession.html', {'name': name})


def delsession(request):
    request.session.flush()
    request.session.clear_expired()
    return render(request, 'delsession.html')



