from django.http import HttpResponse
from django.template import loader
from .models import Users

def Startstrona(request):
  uzytkownicy = Users.objects.all().values()
  template = loader.get_template('uzytkownicy.html')
  context = {
    'uzytkownicy': uzytkownicy,
  }
  return HttpResponse(template.render(context, request))
