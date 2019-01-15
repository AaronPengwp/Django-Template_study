from django.shortcuts import render, HttpResponse, redirect
import datetime
# Create your views here.


class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age  = age

def query(request):

    lists = ["xianming", "lili", "xinhun"]
    lists = []
    dits  ={'name':'Aaron', 'age': 18}

    c = Animal('小熊', '20')

    test = 'hello aarom'
    time = datetime.datetime.utcnow()

    value5 = []
    value6 = '<a href="#">click</a>'

    return render(request,"index.html",locals())



def login(request):

    return HttpResponse("ok")