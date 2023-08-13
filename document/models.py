from django.db import models

class Document(models.Model):
    """
    A model representing a document with a title, content, and publication status.
    """
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=256)
    content = models.TextField()
    published = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title