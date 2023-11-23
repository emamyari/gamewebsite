from django.shortcuts import render

def page1(request):
    a = render(request, 'page1.html')
    return a

def page2(request):
    data={'user':['ali','goli','mohammad','vali']}
    a=render(request,'page2.html',context=data)
    return a
