# sessions/models.py
from django.db import models
from django.conf import settings
from skills.models import Skill   # agar Skill modeli skills appda bo'lsa

class Session(models.Model):
    """Skill almashish sessioni (dars)"""
    
    users = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='user_sessions'
    )
    
    skill = models.ForeignKey(
        Skill,
        on_delete=models.CASCADE,
        related_name='sessions'
    )
    
    status = models.CharField(
        max_length=20,
        choices=[
            ('pending', 'Pending'),
            ('active', 'Active'),
            ('completed', 'Completed'),
        ],
        default='pending'
    )
    
    scheduled_time = models.DateTimeField(null=True, blank=True, help_text="Dars vaqti")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        skill_name = getattr(self.skill, 'name', str(self.skill))
        return f"Session #{self.id} - {skill_name} ({self.status})"

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Session"
        verbose_name_plural = "Sessions"
