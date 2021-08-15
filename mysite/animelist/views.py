from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import User, Anime, Watchlist, CurrentlyWatching, CompletedAnime

def index(request):
    anime_list = Anime.objects.order_by("-title")[:5]
    users = User.objects.order_by("-name")[:5]
    context = {'anime_list': anime_list, 'users': users}
    return render(request, 'animelist/index.html', context)

def anime(request, anime_id):
    anime = get_object_or_404(Anime, pk=anime_id)
    return render(request, 'animelist/anime.html', {'anime': anime})

def user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    watch_list = Watchlist.objects.filter(user__id=user.id)
    currently_watching_list = CurrentlyWatching.objects.filter(user__id=user.id)
    completed_anime = CompletedAnime.objects.filter(user__id=user.id)
    context = {
        'user': user,
        'watch_list': watch_list,
        'currently_watching_list': currently_watching_list,
        'completed_anime': completed_anime,
    }
    print(context)
    return render(request, 'animelist/user.html', context)
