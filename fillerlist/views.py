from django.shortcuts import render
from . import api


def home_page(request):
    context = api.random()
    return render(request, "home_page.html", context)


def search_page(request):
    if request.method == 'GET':
        keyword = request.GET.get('q')
        if not keyword:
            error_page(request)
        else:
            context = api.search(keyword)
            return render(request, "search_page.html", context)
    else:
        error_page(request)


def about_page(request):
    return render(request, "about_page.html")


def anime_page(request, id):
    context = api.anime(id)
    return render(request, "anime_page.html", context)


def error_page(request):
    return render(request, "error_page.html")
