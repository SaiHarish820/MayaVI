from django.db import models

# Create your models here.
class Joinus(models.Model):
    first_name = models.CharField(max_length=10, null=True)
    last_name = models.CharField(max_length=20)
    id_number = models.CharField(max_length=10)
    email = models.CharField(max_length=122)
    comment = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.id_number

