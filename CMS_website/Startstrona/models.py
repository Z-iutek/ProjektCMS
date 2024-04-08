from django.db import models

class Users(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)

class StanStrony(models.Model):
  kolor_tla = models.CharField(max_length=7, default='#FFFFFF')
  tytul_strony = models.CharField(max_length=200, default='Tytuł domyślny')