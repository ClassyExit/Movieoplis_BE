from django.db import models

class SavedItem(models.Model):
    MOVIE = 'movie'
    TV = 'tv'

    ITEM_TYPES = [
        (MOVIE, 'Movie'),
        (TV, 'TV Show'),
    ]

    title = models.CharField(max_length=255)
    overview = models.TextField(blank=True, null=True)
    poster = models.URLField(max_length=500, blank=True, null=True)
    type = models.CharField(max_length=50, choices=ITEM_TYPES)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=['type']),
            models.Index(fields=['title']),
        ]
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} ({self.type})"