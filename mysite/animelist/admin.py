from django.contrib import admin

from .models import Anime, User, Watchlist, CurrentlyWatching, CompletedAnime

admin.site.register(Anime)
admin.site.register(User)
admin.site.register(Watchlist)
admin.site.register(CurrentlyWatching)
admin.site.register(CompletedAnime)
