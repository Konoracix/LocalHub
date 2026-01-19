from django.db import models
from User.models.mixins import TimeStampsMixin
import uuid
from User.enums import Gender

class User(TimeStampsMixin, models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True, blank=False, null=False)
    birth_date = models.DateField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    gender = models.CharField(max_length=1, choices=Gender.choices)
    is_veryfied = models.BooleanField(default=False, blank=True)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)

    location = models.OneToOneField(
        "Location.Location",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="user",
    )