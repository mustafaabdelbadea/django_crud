from django.shortcuts import render
from  django.http import HttpResponse



def landingpage(request):
    return render(request, 'home.html')

