from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import  CreateUserForm
from django.shortcuts import render, get_object_or_404
from .models import NhatKy
from django.contrib.auth import authenticate, login,logout  
from django.contrib.auth.models import User
import markdown



def home(request):
    posts = NhatKy.objects.all()
    print(posts)
    return render(request, 'myBlog/index.html',{'posts': posts})

def postDetail(request, pk):
    post = get_object_or_404(NhatKy, pk=pk)
    post.content_html = markdown.markdown(post.content)
    return render(request, 'myBlog/post-detail.html', {'post': post})

def signUp(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/sign-in') 
        else:
            return redirect('/sign-up')
    else:
        form = CreateUserForm() 
    return render(request, 'myBlog/sign-up.html',{'form': form})


def signIn(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        # print(user)
        if user is not None:
            login(request, user)
            return redirect('/') 
        else:
            return redirect('/sign-in')
    else:
        return render(request, 'myBlog/sign-in.html')


def signOut(request):
    logout(request)
    return redirect('/')