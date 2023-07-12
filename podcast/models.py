from django.db import models


class Tag(models.Model):
    title = models.CharField(max_length=112)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=112)

    def __str__(self):
        return self.title


class Season(models.Model):
    title = models.CharField(max_length=112)
    season_id = models.CharField(max_length=112)


class Podcast(models.Model):
    author = models.ForeignKey('profiles.Profile', on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=112)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    season = models.ForeignKey(Season, null=True, blank=True, on_delete=models.SET_NULL)
    music = models.FileField()
    image = models.ImageField()
    description = models.TextField()
    tag = models.ManyToManyField(Tag)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey('profiles.Profile', on_delete=models.SET_NULL, null=True, blank=True)
    podcast = models.ForeignKey(Podcast, on_delete=models.CASCADE)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.author.user.get_full_name():
            return f"{self.author.user.get_full_name()}'s comment"
        return f"{self.author.user.get_full_name()}'s comment"


class Like(models.Model):
    author = models.ForeignKey('profiles.Profile', on_delete=models.CASCADE)
    music = models.ForeignKey(Podcast, on_delete=models.CASCADE, related_name='music_like')


class Playlist(models.Model):
    author = models.ForeignKey('profiles.Profile', on_delete=models.CASCADE)
    title = models.CharField(max_length=225)

    def str(self):
        return self.title


class PlayListItem(models.Model):
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE, related_name='items')
    episode = models.ForeignKey(Podcast, on_delete=models.CASCADE)


