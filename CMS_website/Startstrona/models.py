from django.db import models

class Users(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)

class StanStrony(models.Model):

  kolor_tla = models.CharField(max_length=12, default='Wpisz kolor')
  tytul_strony = models.CharField(max_length=200, default='Wybierz tytuł')
  nazwa = models.CharField(max_length=100, default='Nazwa zapisu')  # Unikalna nazwa dla każdego stanu
  Naglowek = models.CharField(max_length=200, default='Wpisz naglowek')
  Tekst_glowny = models.TextField(max_length=2000, default='Wpisz tekst glowny')
  Stopka = models.CharField(max_length=200, default='Wpisz stopke')
  Data = models.CharField(max_length=10, default='YEAR-MM-DD')



  def __str__(self):
    return self.nazwa