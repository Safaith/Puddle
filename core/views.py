from django.shortcuts import render,redirect
from django.contrib.auth import logout
from item.models import Category,Item

from .forms import signupform

def index(request):
    categories = Category.objects.all()
    items = Item.objects.filter(is_sold=False)[0:6]
    return render(request,"core/index.html",{
        "categories":categories,
        "items":items
    })

def contact(request):
    return render(request,"core/contact.html")

def signup(request):
    if request.method=="POST":
        form= signupform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = signupform()

    return render(request,"core/signup.html",{
        "form":form
    })

def logoutPage(request):
    logout(request.user)

    return redirect("login")
