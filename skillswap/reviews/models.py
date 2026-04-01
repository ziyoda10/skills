from django.db import models
from django.conf import settings

class Review(models.Model):
    reviewer = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="given_reviews", on_delete=models.CASCADE)
    reviewed_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="received_reviews", on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
