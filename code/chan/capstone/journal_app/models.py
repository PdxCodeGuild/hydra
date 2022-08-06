from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class journalEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    symbol = models.CharField(max_length=50)
    date = models.DateField()
    result = models.IntegerField()
    detail = models.CharField(max_length=1000)
    img_link = models.CharField(max_length=100)

    def __str__(self):
        return self.symbol