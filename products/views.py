from django.http import HttpResponse
from django.shortcuts import render
from .models import Member
from django.template import loader

def myfirst(request):
    products = Member.objects.all().values()
    template = loader.get_template('myfirst.html')
    context = {
        'products': products
    }
    return HttpResponse(template.render(context, request))
  
  
def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())


def all(request):
    template = loader.get_template('all.html')
    return HttpResponse(template.render())


def boy(request):
    template = loader.get_template('boy.html')
    return HttpResponse(template.render())


def accessories(request):
    template = loader.get_template('accessories.html')
    return HttpResponse(template.render())


def men(request):
    template = loader.get_template('men.html')
    return HttpResponse(template.render())


def women(request):
    template = loader.get_template('women.html')
    return HttpResponse(template.render())