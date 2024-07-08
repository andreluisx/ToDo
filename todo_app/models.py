from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Lista(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    detalhes = models.TextField()
    date_modified = models.DateTimeField(auto_now=True, null=True)
    crated_at = models.DateTimeField(auto_now_add=True, null=True)
    done = models.BooleanField(default=False)

    def __str__(self):
        return str(self.title)
