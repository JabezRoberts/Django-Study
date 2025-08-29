from django.shortcuts import render
from .models import Listing


# Create your views here.

# Handles logic and what happens when a user goes to a page on your website
# Have views for CRUD - Create, Retrieve, Update, Delete, List
# Can use functions or classes


# List View
def listing_list(request): 
    
    # Django functions require that you pass one 
    # argument called 'request' that might be coming from the browser and
    # has a lot of information
    
    """ Fetch all the listings in the database using Django ORM - Object Relational Mapper """
    
    listing = Listing.objects.all() # Objects is a property on all Django models that allows you to perform dif operation
    
    context = {
        "listings" : listing
    }
    
    """ We created a dict with our key pointing to listing = Listing.objects.all database call 
    that fetched all the listings then pass it to to context then in the render fxn.
    This context will be injected in the template """
    
    return render(request, "listings.html", context)


# Retrieve
def listing_retrieve(request, pk):
    listing = Listing.objects.get(id=pk)
    context = {
        listing: listing
    }
    
    return render(request, "listings.html", context)