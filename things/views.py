from django.shortcuts import render
from .forms import ThingForm
from .models import Thing


def home(request):
    """Home view."""
    form = ThingForm()
    return render(request, 'home.html', {'form': form})
