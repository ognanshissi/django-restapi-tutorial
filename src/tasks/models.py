from django.db import models

# Create your models here.


class Task(models.Model):
    title = models.CharField(blank=False, max_length=100)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_created=True, blank=True)

    def __str__(self) -> str:
        return f"{self.title} created at {self.created_at}"

    class Meta:
        ordering = ['created_at']
