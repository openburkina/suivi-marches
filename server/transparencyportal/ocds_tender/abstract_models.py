from django.db import models

class Document(models.Model):

    class Meta:
        abstract = True

    document_type = models.CharField(max_length=255) # with choices
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    date_published = models.DateTimeField()
    date_modified = models.DateTimeField()
    document_format = models.CharField(max_length=255) # with choices
    language = models.CharField(max_length=255) # with choices
