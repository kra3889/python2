from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from .models import User
from django.shortcuts import render, redirect
from django.contrib import messages



from django.shortcuts import render
def index(request):
    print ("***** view.py file index function ****")

    return render(request, "beltlogin_set/index.html")
def register(request):
    print ('*************** error function ************')
    result = User.objects.user_validator(request.POST)
    if type(result) == list:
        for err in result:
                messages.error(request, err)
        return redirect('/')
    request.session['user_id'] = result.id
    messages.success(request, "Successfully Registered!")
    return redirect('/success')


    # return redirect('/'+id)

def login(request):
    print ("*********** login page   ***********")
    result = User.objects.login_validator(request.POST)
    if type(result) == list:
        for item in result:
            messages.error(request, item)
        return redirect('/')
    request.session['user_id'] = result.id
    messages.success(request, "Welcom Back, Successfully logged in!")
    return redirect('/success')

def success(request):
    try:
        request.session['user_id']
    except KeyError:
        return redirect('/')
    context = {
        'user': User.objects.get(id=request.session['user_id'])
    }
    return render(request, 'examcdash/success.html', context)

# Create your views here.



# Create your views here.
