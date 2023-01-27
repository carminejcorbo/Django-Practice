from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    date =models.DateTimeField(auto_now=True)
    body = models.TextField()
    
def __str__(self):
    return self.title

    