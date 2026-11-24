
from django.db import models


class Note(models.Model):
    """Represent a sticky note in the database.

    Stores the note title, content and creation date.
    """

    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return the note title as a string.

        :returns: The note title.
        :rtype: str
        """
        return self.title
