from django.shortcuts import render,HttpResponse
from .models import Movie , Genre , Actor , Link , Comment


def movie_view(request):
  movies=Movie.objects.filter(status=True)
  return render(request,'movie/movie_list.html',{'movies':movies})

def movie_detail(request,pk):
  movie=Movie.objects.get(id=pk)
  return render(request,'movie/movie_detail.html',{'movie':movie})





# Funcrional api views 

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MovieSerializer , GenreSerializer , ActorSerializer , LinkSerializer , CommentSerializer



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





from rest_framework.viewsets import ModelViewSet

class Movie_viewset(ModelViewSet):
  queryset=Movie.objects.all()
  serializer_class=MovieSerializer


class Genre_viewset(ModelViewSet):
  queryset=Genre.objects.all()
  serializer_class=GenreSerializer


class Actor_viewset(ModelViewSet):
  queryset=Actor.objects.all()
  serializer_class=ActorSerializer


class Link_viewset(ModelViewSet):
  queryset=Link.objects.all()
  serializer_class=LinkSerializer


class Comment_viewset(ModelViewSet):
  queryset=Comment.objects.all()
  serializer_class=CommentSerializer