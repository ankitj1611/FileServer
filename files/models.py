from django.db import models
from django.contrib.auth.models import User

from os import path, remove
from django.dispatch import receiver
# Create your models here.

class File(models.Model):
    file = models.FileField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
#https://stackoverflow.com/a/16041527    
@receiver(models.signals.post_delete, sender=File)
def file_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `File` object is deleted.
    """
    if instance.file:
        if path.isfile(instance.file.path):
            remove(instance.file.path)        
