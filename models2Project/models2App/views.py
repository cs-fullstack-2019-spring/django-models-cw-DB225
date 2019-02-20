from django.shortcuts import render
from django.http import HttpResponse

# View for the default request
def index(request):
    return HttpResponse("Test")
