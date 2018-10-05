from django.db import models


class RegisteredUser(models.Model):
    email = models.CharField(max_length=50)
    user_id = models.IntegerField(default=0)
    note_count = models.IntegerField(default=0)

    def __str__(self):
        return str(self.email)
