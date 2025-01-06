from django.shortcuts import render ,HttpResponse,redirect
from django.contrib import messages
from .forms import ContactForm
from .models import Contact

def contact(request):
  if request.method=="POST":
    form=ContactForm(request.POST)
    if form.is_valid():
        name=form.cleaned_data['name']
        email=form.cleaned_data['email']
        subject=form.cleaned_data['subject']
        message=form.cleaned_data['message']
        c=Contact()
        c.name=name
        c.email=email
        c.subject=subject
        c.message=message
        c.save()
        return HttpResponse('message sent successfully ')

  else:
     form=ContactForm()
      
  return render(request,'website/contact.html',{'form':form})
