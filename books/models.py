from django.db import models

class Book(models.Model):
        title = models.CharField(max_length=100, unique=True)
        content = models.TextField()
        
        def __unicode__(self):
            return self.title
