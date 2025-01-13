from django.shortcuts import render,HttpResponse
from .models import Movie


def movie_view(request):
  movies=Movie.objects.filter(status=True)
  return render(request,'movie/movie_list.html',{'movies':movies})

def movie_detail(request,pk):
  movie=Movie.objects.get(id=pk)
  return render(request,'movie/movie_detail.html',{'movie':movie})

# Create your views here.

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MovieSerializer



@api_view(["GET"])
def movie_list_api(request):
  moives=Movie.objects.all()
  movies_serilazer=MovieSerializer(moives,many=True)
  return Response(movies_serilazer.data)