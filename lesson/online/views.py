from django.http import HttpResponse
from django.shortcuts import render
from .models import News
from pprint import pprint

def news(request):
    new = News.objects.all()
    all_news = {}
    for i in new:
        # print(i.title,i.created_time.strftime("%d.%m.%Y"))
        a = {
            "title":i.title,
            'time':i.created_time.strftime("%d.%m.%Y")
        }
        all_news.update({i.id:a})
    pprint(all_news)
    return HttpResponse(all_news)


