from django.shortcuts import render, redirect
from .models import Contact


def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'contact_html.html', {'contacts': contacts})



def delete_contact(request, contact_id):
    contact = Contact.objects.get(id=contact_id)
    contact.delete()
    return redirect('contact_list')



