from django.db import models

class AppModel(models.Model):
    isim = models.CharField(max_length=20,name='İsim')
    konu = models.CharField(max_length=100,name='Konu')
    mesaj = models.TextField(name='Mesajınız')
