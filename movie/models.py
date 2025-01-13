from django.db import models
from django.contrib.auth import get_user_model


User=get_user_model()


class Movie(models.Model):
  poster=models.ImageField(upload_to='movie/images/',default="movie/images/1.png")
  title=models.CharField(max_length=255)
  description=models.TextField()
  imdb_score=models.CharField(max_length=50)
  movie_time=models.IntegerField()
  age=models.IntegerField()
  country=models.CharField(max_length=50)
  # rels
  actor=models.ManyToManyField("Actor")
  genre=models.ManyToManyField("Genre")
  author=models.ForeignKey(User, on_delete=models.PROTECT)
  # end rels 
  status=models.BooleanField(default=True)
  created_time=models.DateTimeField( auto_now=False, auto_now_add=True)
  updated_time=models.DateTimeField( auto_now=True, auto_now_add=False)

  def __str__(self):
    return self.title



class Genre(models.Model):
  title=models.CharField(max_length=150,blank=False,null=False)

  def __str__(self):
    return self.title


class Actor(models.Model):
  name=models.CharField(max_length=150)
  bio=models.TextField()

  def __str__(self):
    return self.name


class Link(models.Model):
  movie=models.ForeignKey(Movie, on_delete=models.PROTECT)
  chapter=models.CharField(max_length=150)
  title=models.CharField(max_length=150)
  link=models.TextField()

  def __str__(self):
    return f"{self.chapter} {self.title}"


class Comment(models.Model):
  movie=models.ForeignKey(Movie, on_delete=models.PROTECT)
  name=models.CharField(max_length=150,blank=False,null=False)
  message=models.TextField(blank=False,null=False)
  # opinion=
  status=models.BooleanField(default=True)

  def __str__(self):
    return self.name

