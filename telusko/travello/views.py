from django.shortcuts import render
from .models import Destination
# Create your views here.
# Views is used to define the business logic in the form of template.


def index(request):

    dests = Destination.objects.all()
    return render(request, 'index.html', {'dests': dests})
