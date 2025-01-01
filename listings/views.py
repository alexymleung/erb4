from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from listings.choices import price_choices, bedroom_choices, district_choices
from .models import Listing

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listings, 3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
        'listings': paged_listings
    }
    return render(request,'listings/listings.html',context)

def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)  
    context = {
        "listing": listing,
        }
    return render(request,'listings/listing.html', context)

def search(request):
    queryset_list = Listing.objects.order_by('-list_date')
    if "keywords" in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains = keywords)
    if "title" in request.GET:
        title = request.GET['title']
        if title:
            queryset_list = queryset_list.filter(title__icontains = title)
    if "district" in request.GET:
        district = request.GET['district']
        if district:
            if district != '_':
                queryset_list = queryset_list.filter(district__exact = district)
    if "bedrooms" in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte = bedrooms)
    if "price" in request.GET:
        price = request.GET['price']
        price = float(price)  # Convert to float (or int if preferred)
        if price == 20000001:
            queryset_list = queryset_list.filter(
                    Q(price__gte=price)
                )
        else:
            try:
                queryset_list = queryset_list.filter(
                    Q(price__lte=price) & Q(price__gte=price - 2000000)
                )
            except ValueError:
                # Handle the case where the conversion fails
                # You can log the error or set an error message
                pass  # Or handle the error as needed

    context = {
        'price_choices' : price_choices,
        'bedroom_choices' : bedroom_choices,
        'district_choices' : district_choices,
        'listings' : queryset_list,
        'values' : request.GET,
    }    

    return render(request,'listings/search.html', context)

