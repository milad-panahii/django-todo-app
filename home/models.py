from django.db import models

# class Person(models.Model):
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
    
class Todo(models.Model):
    title = models.CharField(max_length=100)
    # slug = 
    body = models.TextField()
    created = models.DateTimeField()
