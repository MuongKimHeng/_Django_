from django.shortcuts import render, redirect
from .form import PostForm


def index(request):

    return render(request, "post/index.html")


def create(request):

    if request.method == "POST":

        form = PostForm(request.POST)

        if form.is_valid():

            print(form.cleaned_data)

            return redirect("post:index")

    else:

        form = PostForm()

    return render(
        request,
        "post/create.html",
        {
            "form": form
        }
    )