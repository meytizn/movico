from django.shortcuts import render,HttpResponse
from .models import Movie


def movie_view(request):
  movies=Movie.objects.filter(status=True)
  return render(request,'movie/movie_list.html',{'movies':movies})

def movie_detail(request,pk):
  movie=Movie.objects.get(id=pk)
  return render(request,'movie/movie_detail.html',{'movie':movie})

# Create your views here.
