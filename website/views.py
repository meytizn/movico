from django.shortcuts import render ,HttpResponse
# from .models import About

def index(request):
  # about=About.objects.all()
  # context={'about':about}
  return render(request,'website/index.html',)
