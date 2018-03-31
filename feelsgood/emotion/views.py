from django.shortcuts import render
from .Reddit import reddit_scraper
from .apicall import apicall
from django.http import HttpResponse

# emotion
def emotion(request):
    #feels = apicall.getEmotion(request.GET.get('image'))
    link = reddit_scraper.getContent('sad')

    return HttpResponse(link)
