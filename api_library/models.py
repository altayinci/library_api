from django.db import models


class Books (models.Model):

    book_title = models.CharField(max_length=255, null=True, blank=True)
    book_author = models.CharField(max_length=255, null=True, blank=True)

    last_updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.book_title
