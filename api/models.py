from django.db import models
import uuid
# Create your models here.

class Employee(models.Model):
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    dept = models.CharField(max_length=8)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return '%s, %s' % (self.lname, self.fname)
