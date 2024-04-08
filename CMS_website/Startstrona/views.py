from django.http import HttpResponse
from django.template import loader
from .models import Users
from django.shortcuts import render, redirect
from .models import StanStrony
from .forms import StanStronyForm

def Startstrona(request):
    if request.method == "POST":
      form = StanStronyForm(request.POST)
      if form.is_valid():
        form.save()
        return redirect('Startstrona')  # Zaktualizuj, aby odzwierciedlić faktyczną nazwę URL
    else:
      form = StanStronyForm()
      try:
        stan = StanStrony.objects.latest('id')
      except StanStrony.DoesNotExist:
        stan = None

    return render(request, 'Startstrona/uzytkownicy.html', {'form': form, 'stan': stan})