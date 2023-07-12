from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=112)

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=112)

    def __str__(self):
        return self.title
# yasg pillow django rest_framework

class Article(models.Model):
    author = models.ForeignKey("profiles.Profile", on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=112)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='articles/')
    description = models.TextField()
    tags = models.ManyToManyField(Tag)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
