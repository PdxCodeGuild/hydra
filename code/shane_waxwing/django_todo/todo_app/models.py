from django.db import models

# Create your models here.

class ToDoItem(models.Model):
    description = models.TextField(max_length=50)
    created_date = models.DateField()
    completed_date = models.DateField(blank=True, null=True)
    completed_boolean = models.BooleanField()

    def __str__(self):
        return self.description