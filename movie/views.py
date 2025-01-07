from django.shortcuts import render,HttpResponse



def movie_view(request):
  return render(request,'movie/movie_list.html')



# Create your views here.
