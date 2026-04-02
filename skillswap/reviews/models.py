# from django.db import models
# from django.conf import settings

# class Review(models.Model):
#     reviewer = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="given_reviews", on_delete=models.CASCADE)
#     reviewed_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="received_reviews", on_delete=models.CASCADE)
#     rating = models.IntegerField()
#     comment = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)

from django.db import models
from django.conf import settings
from skills_sessions.models import Session

class Rating(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE, related_name='ratings')
    from_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='given_ratings')
    to_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='received_ratings')
    stars = models.IntegerField()
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('session', 'from_user', 'to_user')

    def __str__(self):
        return f"{self.from_user} → {self.to_user}: {self.stars}⭐"
