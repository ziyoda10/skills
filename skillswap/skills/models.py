from django.db import models
from django.conf import settings

class Skill(models.Model):
    LEVEL_CHOICES = (
        ("beginner", "Beginner"),
        ("intermediate", "Intermediate"),
        ("advanced", "Advanced"),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES)
    is_teaching = models.BooleanField()  # True = o‘rgatadi, False = o‘rganmoqchi

    def __str__(self):
        return f"{self.user.username} - {self.name}"
