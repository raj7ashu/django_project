from django.shortcuts import render, redirect
from .models import Listing
from .forms import ListingForm

# Create your views here.
def index(request):
    return render(request, 'listings/index.html')

def greetings(request):
    return render(request,"listings/greetings.html")

def all_listings(request):
    all_listings = Listing.objects.order_by('-list_date')
    context = {'all_listings': all_listings}
    return render(request, 'listings/all_listings.html',context)

def new_listing(request):
    if request.method !="POST":
        form = ListingForm()
    else:
        form = ListingForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            return redirect('listings:all_listings')
    context = {'form': form}
    return render(request,'listings/new_listing.html',context)