from datetime import datetime

from django.shortcuts import render


def page1(request):
    a = render(request, 'page1.html')
    return a

def page2(request):
    data={'user':'emamyari'}
    a=render(request,'page2.html',context=data)
    return a