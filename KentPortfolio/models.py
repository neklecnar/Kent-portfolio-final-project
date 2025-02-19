from django.db import models

class Contact(models.Model):
    fname = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.fname
