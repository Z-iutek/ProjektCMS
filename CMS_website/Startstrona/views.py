from django.shortcuts import render, get_object_or_404, redirect
from .models import StanStrony
from .forms import StanStronyForm

# Widok do wyświetlania listy stanów i formularza do ich zapisu
def Startstrona(request):
    form = StanStronyForm(request.POST or None)
    stany = StanStrony.objects.all()  # Pobranie wszystkich stanów z bazy danych przed blokami warunkowymi

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('Startstrona')

    return render(request, 'Startstrona/uzytkownicy.html', {'form': form, 'stany': stany})

# Widok do przywracania wybranego stanu
def przywroc_stan(request, stan_id):
    stan = get_object_or_404(StanStrony, pk=stan_id)
    # Tutaj możesz dodać logikę do przywrócenia stanu, np. przekierowanie z odpowiednimi danymi
    return render(request, 'Startstrona/przywroc.html', {'stan': stan})
