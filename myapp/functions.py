import json

import requests
from django.shortcuts import render
import http.client


def page2(request):

    data=requests.get('https://api.digikala.com/v1/promotions/plp_63247410/?has_selling_stock=1&sort=7&seo_url=&page=2').text
    d=json.loads(data)
    a=render(request,'page2.html',d)
    return a

def products(request):
    data=requests.get('https://api.digikala.com/v1/categories/wearable-gadget/search/?brands%5B0%5D=10&camCode=582&seo_url=%2Fcategory-wearable-gadget%2F%3Fbrands%255B0%255D%3D10%26camCode%3D582&page=1').text
    d=json.loads(data)

    a=render(request,'products.html',context=d)
    return a