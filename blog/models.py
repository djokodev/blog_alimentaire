from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name="Nom de l'article")
    desc = models.TextField()
    image = models.ImageField(upload_to="articles")
    created_at = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
