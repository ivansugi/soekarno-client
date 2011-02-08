from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.forms import ModelForm

class TempSession(models.Model):
    server_user_id = models.IntegerField()
    server_token = models.CharField(max_length=254)
    client_session_key = models.CharField(max_length=254)

class ServerUser(models.Model):
    server_user_id = models.IntegerField()
    client_user_id = models.ForeignKey(User)