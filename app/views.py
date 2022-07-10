from django.shortcuts import render
import requests

# Create your views here.

# api_v1 = {'all':"https://inshortsapi.vercel.app/news?category", 'sports':"https://inshortsapi.vercel.app/news?category=sports", 'entertain':"https://inshortsapi.vercel.app/news?category=entertainment", 'science':"https://inshortsapi.vercel.app/news?category=science", 'business':"https://inshortsapi.vercel.app/news?category=business",'world':"https://inshortsapi.vercel.app/news?category=world",'default':"https://inshortsapi.vercel.app/news?category="}

api_v2 = "https://inshorts.deta.dev/news?category="


def index(request):
    respoce = requests.get(api_v2)
    api_data = respoce.json()
    return render(request, 'index.html', {'api_data': api_data})


def about(request):
    return render(request, 'about.html')


def sports(request):
    respoce = requests.get(api_v2 + 'sports')
    api_data = respoce.json()

    return render(request, 'sports.html', {'api_data': api_data})


def entertain(request):
    respoce = requests.get(api_v2 + 'entertainment')
    api_data = respoce.json()

    return render(request, 'entertain.html', {'api_data': api_data})


def science(request):
    respoce = requests.get(api_v2 + 'science')
    api_data = respoce.json()

    return render(request, 'science.html', {'api_data': api_data})


def business(request):
    respoce = requests.get(api_v2 + 'business')
    api_data = respoce.json()

    return render(request, 'business.html', {'api_data': api_data})


def world(request):
    respoce = requests.get(api_v2 + 'world')
    api_data = respoce.json()

    return render(request, 'world.html', {'api_data': api_data})


def national(request):
    respoce = requests.get(api_v2 + 'national')

    api_data = respoce.json()

    return render(request, 'others.html', {'api_data': api_data})


def technology(request):
    respoce = requests.get(api_v2 + 'technology')
    api_data = respoce.json()

    return render(request, 'others.html', {'api_data': api_data})


def startup(request):
    respoce = requests.get(api_v2 + 'startup')
    api_data = respoce.json()

    return render(request, 'others.html', {'api_data': api_data})


def hatke(request):
    respoce = requests.get(api_v2 + 'hatke')
    api_data = respoce.json()

    return render(request, 'others.html', {'api_data': api_data})


def automobile(request):
    respoce = requests.get(api_v2 + 'automobile')
    api_data = respoce.json()

    return render(request, 'others.html', {'api_data': api_data})


def politics(request):
    respoce = requests.get(api_v2 + 'politics')
    api_data = respoce.json()

    return render(request, 'others.html', {'api_data': api_data})
