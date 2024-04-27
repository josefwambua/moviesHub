import requests
from django.shortcuts import render


def home(request):
  # Fetching movie data from the TMDB API
  APILINK = 'https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key=1a6c1a09a92f40dfa8f3c6dc254af26b&page=1'
  response = requests.get(APILINK)
  data = response.json()
  movies = data.get('results', [])

  return render(request, 'templates/index.html', {'movies': movies})


def about(request):
  return render(request, 'about.html')


def recently_watched(request):
  return render(request, 'recently_watched.html')


def wishlist(request):
  return render(request, 'wishlist.html')
