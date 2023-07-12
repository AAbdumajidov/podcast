from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=225)

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=225)

    def __str__(self):
        return self.title


class Season(models.Model):
    title = models.IntegerField()


class Episode(models.Model):
    singer = models.ForeignKey('singer.Singer', on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=225)
    description = models.TextField()
    season = models.ForeignKey(Season, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(upload_to='articles')
    song = models.FileField(upload_to='files')
    created_date = models.DateTimeField(auto_now_add=True)

    tag = models.ManyToManyField(Tag)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='categor')

    def __str__(self):
        return self.title
    # def __str__(self):
    #     if self.singer.get_full_name() != ' ':
    #         return f"{self.singer.get_full_name}"
    #     return f"{self.singer.username}"


class Music(models.Model):
    author = models.ForeignKey("singer.Singer", on_delete=models.CASCADE)
    title = models.CharField(max_length=221)
    text = models.TextField()
    season = models.ForeignKey(Season, null=True, blank=True, on_delete=models.SET_NULL)
    image = models.ImageField(upload_to="music.images/")
    music = models.FileField('musics/')
    created_date = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    author = models.ForeignKey('singer.Singer', on_delete=models.SET_NULL, related_name='podcast_com_author', null=True, blank=True)
    article = models.ForeignKey(Episode, on_delete=models.CASCADE, related_name='comment')
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=225, null=True, blank=True)
    is_anonymous = models.BooleanField(default=False, null=True, blank=True)
    image = models.ImageField(upload_to='article', null=True, blank=True)

    # def __str__(self):
    #     if self.author.user.get_full_name():
    #         return f"{self.author.user.get_full_name()}'s comment"
    #     return f"{self.author.user.username}'s comment"

    class Meta:
        ordering = ['-id']


class Like(models.Model):
    author = models.ForeignKey('singer.Singer', on_delete=models.CASCADE)
    music = models.ForeignKey(Episode, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['author', 'music'], name="unique_like"),
        ]


class Playlist(models.Model):
    author = models.ForeignKey('singer.Singer', on_delete=models.CASCADE)
    title = models.CharField(max_length=225)

    def str(self):
        return self.title


class PlayListItem(models.Model):
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE, related_name='items')
    episode = models.ForeignKey(Episode, on_delete=models.CASCADE)
