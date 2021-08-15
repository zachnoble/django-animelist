from django.db import models

class Anime(models.Model):
    title = models.CharField(max_length=250)
    synopsis = models.TextField()
    # mean = 
    # rank =
    # popularity =
    # nsfw =
    # genres =
    # num_episodes =
    # start_season =
    # rating =
    # studios =
    # statistics =

    def __str__(self):
        return self.title

class User(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()

    def __str__(self):
        return self.name + " " + str(self.age)

class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.name + " " + self.anime.title


class CurrentlyWatching(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.name + " " + self.anime.title

class CompletedAnime(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.name + " " + self.anime.title

