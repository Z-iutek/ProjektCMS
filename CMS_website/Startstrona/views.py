from django.http import HttpResponse
from django.template import loader

def Startstrona(request):
  template = loader.get_template('glowna.html')
  return HttpResponse(template.render())