from django.db import models

class Destination(models.Model):
    place_name = models.CharField(max_length=200)
    weather = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    google_map_link = models.URLField(max_length=500, blank=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='images/', default='default.jpg')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.place_name
