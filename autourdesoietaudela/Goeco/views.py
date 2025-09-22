from django.shortcuts import render
from django.utils.timezone import now
# Create your views here.

def home(request):
    return render(request, 'Goeco/base.html', {'timestamp': int(now().timestamp())})
