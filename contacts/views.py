from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact

def contact(request):
    if request.method =='POST':
        listing_id=request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        user_id = request.POST['user_id']
        message = request.POST['message']
        advisor_email = request.POST['advisor_email']

        #check if user maede any inquery
        if request.user.is_authenticated:
            user_id=request.user.id
            has_contacted=Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'you have already made request for this place')
                return redirect('/listings/' + listing_id)

        contact= Contact(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone, message=message, user_id=user_id)
        contact.save()



        messages.success(request, 'your request has been submitted succesfully, our advisor will get back to you as soon as possible')
        return redirect('/listings/'+listing_id)

