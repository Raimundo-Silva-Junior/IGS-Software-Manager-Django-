from uuid import uuid4
from django.db import models

# Create your models here.

class Employee(models.Model):
    id_employee = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    department = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name, self.email, self.department
    
        