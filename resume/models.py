from django.db import models

# Create your models here.
class cv(models.Model):
    name = models.CharField(max_length=100)
    education = models.TextField()
    experience = models.TextField()
    # Add more fields as needed

    def __str__(self):
        return self.name