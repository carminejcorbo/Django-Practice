from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField( max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    message = models.TextField(max_length=20, blank=True,null=True)
    
def __str__(self):
    return self.subject

# from django.db import models

# class Contact(models.Model):
# 	name=models.CharField(max_length=200, blank=True, null=True)
# 	email=models.CharField(max_length=20, blank=True, null=True)
# 	subject=models.CharField(max_length=20, blank=True,                     null=True)
# 	def __str__(self):
# 		return self.name
   