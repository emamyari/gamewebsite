import json

import requests
from django.shortcuts import render
import http.client


def page2(request):

    data=requests.get('https://api.digikala.com/v1/promotions/plp_63247410/?has_selling_stock=1&sort=7&seo_url=&page=2').text
    d=json.loads(data)
    a=render(request,'page2.html',d)
    return a
