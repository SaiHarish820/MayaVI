from django.db import models

# Create your models here.
class Joinus(models.Model):
    name = models.CharField(max_length=10, null=True)
    id_num = models.CharField(max_length=10)
    email = models.CharField(max_length=122)
    message = models.TextField()
    date = models.DateField()
    def __str__(self):
        return self.id

