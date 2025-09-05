from django.shortcuts import render, redirect
from .models import Listing
from .forms import ListingForm


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

# Need form to create and update
def listing_create(request):
    # if request.method == "POST":
    #     form = ListingForm(request.POST)
    #     if form.is_valid():
    #         #TODO
    #         pass
    #     context = {
    #         "form": form
    #     }
    #     return render(request, "listing_create.html", context)
        
    # form = ListingForm()
    # context = {
    #     "form": form
    # }
    # return render(request, "listing_create.html", context)
    
    form = ListingForm()
    if request.method == "POST":
        form = ListingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save() # create a new listing with the entered data. Save entered data
            # to the database
            return redirect("/")
    context = {
        "form": form
    }
    return render(request, "listing_create.html", context)



# Listing update view
def listing_update(request, pk):    
    listing = Listing.objects.get(id=pk)
    form = ListingForm(instance=listing) # The instance to update is this specific listing
    
    if request.method == "POST":
        form = ListingForm(request.POST, instance=listing, files=request.FILES)
        if form.is_valid():
            form.save() # create a new listing with the entered data. Save entered data
            # to the database
            return redirect("/")
    context = {
        "form": form
    }
    return render(request, "listing_update.html", context)


# Delete view
def lisitng_delete(request, pk):
    listing = Listing.objects.get(id=pk)
    listing.delete()
    return redirect("/")