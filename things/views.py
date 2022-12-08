from django.shortcuts import render
from .forms import ThingForm
from .models import Thing


def home(request):
    """Home view."""
    submitted = False
    if request.method == 'POST':
        form = ThingForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ThingForm()
        if 'submitted' in request.GET:
            submitted = True

    

    return render(request, 'home.html', {'form': form, 'submitted': submitted})
