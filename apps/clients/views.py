from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.validators import email_re
from Crypto.PublicKey import RSA
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

from clients.models import TempSession
import logging


def connect(request, template_name="clients/connect.html"):
    logging.debug('connect')
    return render_to_response(template_name, context_instance=RequestContext(request))
    
def claim_data(request, token, template_name="clients/connect.html"):
    logging.debug('connect')
    #get token
    temp = TempSession.objects.get(server_token = token)
    user = User.objects.get(id = temp.server_user_id)
    if user is not None : 
        if user.is_active :
            #user_login = authenticate(username=user.username, password=user.password)
            print('autheticating')
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            login(request, user)
            
            temp.client_session_key = request.session.session_key
            temp.save()
            return HttpResponse("data claimed")
    return HttpResponse("user failed")

@csrf_exempt
def consumer(request):
    logging.debug('connect')
    #get send data
    logging.debug('connect123')
    if request.user.is_authenticated() :
        return HttpResponse("user is logged in")
    else :
        if request.method == 'POST':
            try :
                if (request.POST['token']) :
                    #print request.POST['token']
                    #print request.POST['id']
                    temp = TempSession.objects.create(server_user_id = request.POST['id'] ,server_token = request.POST['token'])
                    temp.save()
                    #print temp
                    return HttpResponse("saved")
                else :
                    return HttpResponse("failed")
            except :
                return HttpResponse("failed")
    return HttpResponse("loggedin")

def not_user(request, template_name="clients/connect.html"):
    logging.debug('connect')
  
    return HttpResponse("not user")
@login_required
def logout(request, template_name="clients/connect.html"):
    logging.debug('connect')
    return HttpResponse("user")