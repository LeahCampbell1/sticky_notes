from django.db import models


# Define attributes for sql table
# Used course material "Django Sticky Notes application.pdf"
# for reference to note model format
class Note(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    # Define string method for outputting string
    def __str__(self):
        return self.title
