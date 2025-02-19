from django.db import models

class ListItem(models.Model):
    MOVIE = 'movie'
    TV = 'tv'

    ITEM_TYPES = [
        (MOVIE, 'Movie'),
        (TV, 'TV Show'),
    ]

    firebase_uid = models.CharField(max_length=100)
    item_id = models.IntegerField(blank=False, null=False, default=0)
    title = models.CharField(max_length=255)
    overview = models.TextField(blank=True, null=True)
    poster = models.URLField(max_length=500, blank=True, null=True)
    type = models.CharField(max_length=50, choices=ITEM_TYPES)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=['firebase_uid']),
            models.Index(fields=['title']),
        ]
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.firebase_uid} ({self.title})"