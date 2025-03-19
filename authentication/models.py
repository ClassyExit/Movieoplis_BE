from django.db import models
import uuid

class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    firebase_uid = models.CharField(max_length=100, unique=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    canViewVideos = models.BooleanField(default=False)
    isAdmin = models.BooleanField(default=False)


    
    def __str__(self):
        return self.firebase_uid


class UserVideoPermissionQueue(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    firebase_uid = models.CharField(max_length=100, unique=True, db_index=True)


    def __str__(self):
        return self.firebase_uid + 'Queue'