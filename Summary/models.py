from django.db import models

class Documents(models.Model):
    docname = models.CharField(max_length=50)
    keywords = models.TextField(max_length=100,default='')
    file = models.FileField(upload_to='data/')

    def __unicode__(self):
        return self.file.name

    class Meta:
        ordering = ['-pk']