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


@api_view(["GET"])
def movie_detail_api(request,pk):
  movie=Movie.objects.get(id=pk)
  movie_serializer=MovieSerializer(movie,many=False)
  return Response(movie_serializer.data)


@api_view(["POST"])
def movie_create_api(request):
  movie_post=MovieSerializer(data=request.data)
  if movie_post.is_valid():
    movie_post.save()
  return Response(movie_post.data)



@api_view(["POST"])
def movie_update_api(request,pk):
  instance=Movie.objects.get(id=pk)
  movie_post=MovieSerializer(instance,data=request.data)
  if movie_post.is_valid():
    movie_post.save()
  return Response(movie_post.data)  



@api_view(["DELETE"])
def movie_delete_api(request,pk):
  movie=Movie.objects.get(id=pk)
  movie.delete()
  return Response("movie deleted successfully ")