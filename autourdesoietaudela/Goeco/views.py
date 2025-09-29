from django.shortcuts import render
from django.utils.timezone import now
from .models import Composteur, RecyclerieRessourcerie

# Create your views here.

def home(request):
    return render(request, 'Goeco/base.html', {'timestamp': int(now().timestamp())})

def composteur_page(request):
    composteurs = Composteur.objects.all()
    context = {
        'composteurs': composteurs,
        'timestamp': int(now().timestamp()),
    }
    return render(request, 'Goeco/composteur_page.html', context)
