from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.utils.text import slugify
from django.urls import reverse
from math import floor


class Movies(models.Model):
    title = models.CharField(max_length=50)
    director = models.CharField(max_length=50)
    rating = models.IntegerField(validators=[
        MinLengthValidator(1),
        MaxLengthValidator(10)
    ])
    duration = models.IntegerField(null=False)
    release_year = models.IntegerField(null=False)
    slug = models.SlugField(null=False, db_index=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("movie_details", args=[self.slug])

    def __str__(self):
        return f"Title: {self.title}, director: {self.director}, rating: {self.rating}, duration: {self.duration}, release year: {self.release_year}, slug: {self.slug}"
    
    def duration_converter(self):
        hours = floor(self.duration / 60)
        minutes = (self.duration) - hours * 60
        return f"{hours}h {minutes}m"
