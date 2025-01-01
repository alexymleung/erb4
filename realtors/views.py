from django.shortcuts import render, get_object_or_404
from .models import Realtor

def realtor(request, realtor_id):
    realtor = get_object_or_404(Realtor, pk=realtor_id)  
    context = {
        "realtor": realtor,
        }
    return render(request,'realtors/realtor.html', context)

