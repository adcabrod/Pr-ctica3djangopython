from django.db import models
from django.contrib.auth.models import User










class Categoria (models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name








class Post(models.Model):
    owner = models.ForeignKey(User)
    title = models.CharField(max_length=50)
    url = models.URLField(null=True)
    introduction = models.CharField(max_length=300, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    publication_date = models.DateTimeField()
    categories = models.ManyToManyField(Categoria)

    def __str__(self):
        return self.title
