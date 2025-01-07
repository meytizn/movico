from django.shortcuts import render,HttpResponse
from .models import Movie


def movie_view(request):
  movies=Movie.objects.all()
  return render(request,'movie/movie_list.html',{'movies':movies})



# Create your views here.
