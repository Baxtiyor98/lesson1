from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import News
from pprint import pprint
from .forms import *

def news(request):
    new = News.objects.all()
    all_news = []
    for i in new:
        # print(i.title,i.created_time.strftime("%d.%m.%Y"))
        print(i.imageURL)
        a = {
            'id':i.id,
            'cat':i.category.name,
            "title":i.title,
            "image":i.imageURL,
            "desc":i.description,
            'time':i.created_time.strftime("%d.%m.%Y")
        }
        all_news.append(a)
    # pprint(all_news)
    return render(request,'news.html',context={'yangiliklar':all_news})

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