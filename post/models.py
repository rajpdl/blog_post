from django.db import models
from account.models import User

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    author_id = models.ManyToManyField(User)

    def __str__(self):
        return self.title
    
    def short(self):
        return self.body[:100]

