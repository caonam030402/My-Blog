from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CreateUserForm
from django.shortcuts import render, get_object_or_404
from .models import NhatKy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
import markdown


def home(request):
    posts = NhatKy.objects.all()
    for post in posts:
        print(post.created_at)
    return render(request, "myBlog/index.html", {"posts": posts})


def postDetail(request, pk):
    post = get_object_or_404(NhatKy, pk=pk)
    post.content_html = markdown.markdown(post.content)
    return render(request, "myBlog/post-detail.html", {"post": post})


def signUp(request):
    if request.user.is_authenticated:
        return redirect("/")

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            if form.cleaned_data["password1"] != form.cleaned_data["password2"]:
                form.add_error("password2", "Passwords do not match")
                return render(request, "myBlog/sign-up.html", {"form": form})
            else:
                form.save()
                return redirect("/sign-in")
    else:
        form = CreateUserForm()

    return render(request, "myBlog/sign-up.html", {"form": form})


def signIn(request):
    if request.user.is_authenticated:
        return redirect("/")

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if not username or not password:
            return render(
                request,
                "myBlog/sign-in.html",
                {"error": "Please provide both username and password."},
            )

        print("Username:", username)  # Debugging statement
        print("Password:", password)  # Debugging statement

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            print("1")
            return render(
                request,
                "myBlog/sign-in.html",
                {"error": "Invalid username or password."},
            )

    return render(request, "myBlog/sign-in.html")


def signOut(request):
    logout(request)
    return redirect("/sign-in")
