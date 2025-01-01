from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact
from listings.models import Listing

def contact(request):
    if request.method == "POST":
        listing_id = request.POST["listing_id"]
        listing_title = request.POST["listing_title"]
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        message = request.POST["message"]
        user_id = request.POST["user_id"]
        realtor_email = request.POST["realtor_email"]
        if request.user.is_authenticated:
            user_id = request.user.id
            has_enquired = Contact.objects.all().filter(listing_id = listing_id, user_id = user_id)
            if has_enquired:
                messages.error(request, "You have made an enquiry for this listing before, we will contact you soon!")
                return redirect('/listings/'+listing_id)
            listing_obj = get_object_or_404(Listing, pk=listing_id)
            contact = Contact(
                listing=listing_title, 
                listing_id=listing_obj,
                name=name, 
                email=email, 
                phone=phone, 
                message=message, 
                user_id=user_id,
                )
            contact.save()
            # send_mail(
            #     "Listing Enquiry",
            #     "Enquiry for " + listing_title + ". Sign into admin for more info",
            #     "admin@bcrealestate.hk",                    # from
            #     [realtor_email, 'boss@bcrealestate.hk'],    # to & cc
            #     fail_silently=False
            # )
            messages.success(request, "Your request submitted, we will contact you very soon")
        return redirect('/listings/'+listing_id)

