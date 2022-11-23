from django.db import models


class Recipe(models.Model):
    author = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    brief_description = models.TextField()
    full_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-created_at",)

    # def __str__(self):
    #     return self.title
