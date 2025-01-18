
from django.db import models

class FileUpload(models.Model):
    name = models.CharField(max_length=255)  # File name
    file = models.FileField(upload_to='uploads/')  # File storage path
    uploaded_at = models.DateTimeField(auto_now_add=True)  # Upload timestamp

    def __str__(self):
        return self.name

