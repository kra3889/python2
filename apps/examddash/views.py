from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect, HttpResponse
from ..beltlogin_set.models import User
from django.contrib import messages
from datetime import datetime, date

# Create your views here.
def success(request):
    user2=request.session['user_id']
    try:
        request.session['user_id']
    except KeyError:
        return redirect('/')
    this_user=request.session['user_id']
    now = date.today()



    print("***count of today*****now", now)

    context = {
        'user': User.objects.get(id=request.session['user_id']),
        'people':User.objects.exclude(id=request.session['user_id']),
        'mypokes':User.objects.filter(poke=this_user),
        'usercnt': User.objects.filter(poke=this_user).count(),
        }

    return render(request, 'examcdash/success.html', context)

def logout(request):
    try:
        #print('**** return render ****')
        return render(request, 'beltlogin_set/index.html')
    except KeyError:
        #print('**** redirect ****')
        return redirect('/')

def examdpoke(request, id):
    user2=request.session['user_id']
    pokeid = id
    print("************ examdpoke")
    result=User.objects.examdpoke(request.POST, pokeid, user2)
    if type(result) == list:
        print("************* review result list*******************")
        for item in result:
            messages.error(request, item)
        return redirect('/')
    print("********examdpoke*************")


    return  redirect ('/success' )
