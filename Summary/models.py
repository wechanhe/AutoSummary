from django.db import models
from django.db.models.signals import post_delete
import os

class Documents(models.Model):
    docname = models.CharField(max_length=50)
    keywords = models.TextField(max_length=100,default='')
    file = models.FileField(upload_to='./Summary/data/')

    def __unicode__(self):
        return self.file.name

    class Meta:
        ordering = ['-pk']


def delete_file(sender, **kwargs):
    patch = kwargs['instance']
    os.remove(patch.file.path)

post_delete.connect(delete_file, sender=Documents)