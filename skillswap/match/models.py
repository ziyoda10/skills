from django.db import models
from django.conf import settings
from skills.models import Skill


class Match(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="sent_matches", on_delete=models.CASCADE)
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="received_matches", on_delete=models.CASCADE)
    skill = models.CharField(max_length=100)
    status = models.CharField(max_length=20, default="pending")  # pending, accepted, rejected
    created_at = models.DateTimeField(auto_now_add=True)




class Match(models.Model):
    sender = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="sent_matches"
    )
    receiver = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="received_matches"
    )
    skill = models.ForeignKey(
        Skill,
        on_delete=models.CASCADE
    )
    status = models.CharField(
        max_length=20,
        choices=[
            ('pending', 'Pending'),
            ('accepted', 'Accepted'),
            ('rejected', 'Rejected'),
        ],
        default="pending"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender} -> {self.receiver} ({self.status})"



