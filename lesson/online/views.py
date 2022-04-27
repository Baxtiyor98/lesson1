from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import News

from .forms import *

def news(request):
    cats = Category.objects.all()
    return render(request,'news.html',context={'cats': cats})

def cats(request,id):
    print(type(id))
    new = News.objects.filter(category_id=id)
    all_news = []
    for i in new:
        a = {
            'id':i.id,
            "title":i.title,
            "image":i.imageURL,
            "desc":i.description,
            'time':i.created_time.strftime("%d.%m.%Y")
        }
        all_news.append(a)
    return render(request,'cats.html',context={'news':all_news,
                                               "name":Category.objects.get(id=id).name})

def search(request):
    print(request.method)
    if request.method=="POST":
        text = request.POST.get('search')
        news = News.objects.filter(title__icontains=text)
        print(news)
    return render(request,'search.html',context={'news':news})

def info(request,id):
    return render(request,'info.html',{'info':News.objects.get(id=id)})

def add(request):
    form = Yangiliklar()
    if request.method=="POST":
        form = Yangiliklar(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('news')
    return render(request,'post.html',{"form":form})

def update(request,id):
    new = News.objects.get(id=id)
    form = Yangiliklar(instance=new)
    print(request.method)
    if request.method=="POST":
        form = Yangiliklar(request.POST,request.FILES,instance=new)
        if form.is_valid():
            form.save()
            return redirect('news')
    return render(request,'update.html',{"form":form,
                                       'title':new.title})

def delete(request,id):
    News.objects.get(id=id).delete()
    return redirect('news')

def register(request):
    form = Registration(request.POST)
    if request.method=="POST":
        if form.is_valid():
            form.save()
            username = request.POST['username']
            password = request.POST['password1']
            email = request.POST['email']
            user = authenticate(request, username=username, password=password, email=email)
            print(user)
            if user:
                login(request,user)
                return redirect('news')
    return render(request,'register.html',{"form":form})

def log_in(request):
    form = Login()
    if request.method=="POST":
        form = Login(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            print(username,password)
            user = authenticate(request, username=username, password=password)
            print(user)
            if user:
                login(request,user)
                return redirect('news')
    return render(request,'login.html',{"form":form})

def log_out(request):
    logout(request)
    return redirect('log_in')
