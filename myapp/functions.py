import json

import pyodbc
import requests
from django.shortcuts import render
import http.client
from rest_framework.decorators import api_view


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

def daf(request):
    connection = pyodbc.connect(
        'DRIVER={ODBC DRIVER 17 FOR SQL SERVER};Server=192.168.1.56;Database=emamyari;Port=1433;UID=sa;PWD=111')
    cursor=connection.cursor()
    cursor.execute("select * from digi")
    data=cursor.fetchall()

    return render(request,'persons.html',{'data':data})

def Amin (request):
    connection = pyodbc.connect(
        'DRIVER={ODBC DRIVER 17 FOR SQL SERVER};Server=192.168.1.56;Database=Mono0_0;Port=1433;UID=sa;PWD=111')
    cursor=connection.cursor()
    cursor.execute("select * from pro")
    data=cursor.fetchall()

    return render(request,'prds.html',{'data':data})
def Karname(request):
    connection = pyodbc.connect(
        'DRIVER={ODBC DRIVER 17 FOR SQL SERVER};Server=192.168.1.56;Database=Mono0_0;Port=1433;UID=sa;PWD=111')
    cursor=connection.cursor()
    cursor.execute("select * from PayanTahsili")
    data=cursor.fetchall()

    return render(request,'Karname.html',{'data':data})

@api_view(['GET','POST'])
def register(request):
    if request.method=='POST':
        print(request.data['name'])
        print(request.data['price'])
        print(request.data['color'])
        print(request.data['weight'])
        print(request.data['madein'])
    return render(request,'register.html')