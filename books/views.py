from django.http import HttpResponse
from django.shortcuts import render


def index_page(request):
    return HttpResponse('<h1>Hello world!!!2</h1>')

