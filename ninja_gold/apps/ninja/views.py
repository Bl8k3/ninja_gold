# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import random
import datetime
from django.shortcuts import render

# Create your views here.
def index(request):
    if request.session.get('gold') is None:
        request.session['gold']=0
    if request.session.get('Log') is None:
        request.session['Log']=""
    return render(request,'index.html')
    


def generate(request,building):
    print "posting request"
    if building=='farm':
        farmGold=random.randint(10,21)
        request.session['gold']+=farmGold
        request.session['Log']="You got {} gold {}".format(farmGold,(datetime))
        return render(request,'index.html')
    print "posting request"
    if building =='cave':
        caveGold=random.randint(5,10)
        request.session['gold']+=caveGold
        request.session['Log']="You got {} gold {}".format(caveGold,(datetime))
        return render(request,'index.html')
    print "posting request"
    if building=='house':
        houseGold=random.randint(2,5)
        request.session['gold']+=houseGold
        request.session['Log']="You got {} gold {}".format(houseGold,(datetime))
        return render(request,'index.html')
    print "posting request"
    if building=='casino':
        casinoGold=random.randint(-100,5000000)
        request.session['gold']+=casinoGold
        request.session['gold']-=casinoGold
        request.session['Log']="You lost {} gold ! Tough luck...{}".format(casinoGold,(datetime))
        return render(request,'index.html')