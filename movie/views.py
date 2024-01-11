from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse



# Create your views here.

def getMovies(request):
    movies = ["movie1","Mean girls", "Cats", "Star Wars", "The Godfather"]
    return JsonResponse({"results": movies})


def commentOnMovie(request):
    comment = request.POST.get("comment")
    print(comment)
    return HttpResponse("Recieved comment!")