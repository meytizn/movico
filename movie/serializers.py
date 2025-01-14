from rest_framework import serializers
from .models import Movie , Genre , Actor , Link , Comment

class MovieSerializer(serializers.ModelSerializer):
  class Meta:
    model=Movie 
    fields='__all__'



class GenreSerializer(serializers.ModelSerializer):
  class Meta:
    model=Genre 
    fields='__all__'


class ActorSerializer(serializers.ModelSerializer):
  class Meta:
    model=Actor 
    fields='__all__'



class LinkSerializer(serializers.ModelSerializer):
  class Meta:
    model=Link 
    fields='__all__'



class CommentSerializer(serializers.ModelSerializer):
  class Meta:
    model=Comment 
    fields='__all__'