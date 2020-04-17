from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from listings.choices import state_choices

def index(request):
    listings= Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    context={
        'listings':listings,
        'state_choices': state_choices
    }
    return render(request, 'pages/index.html', context)

def about(request):
    return render(request, 'pages/about.html')

