from django.db import models
from django.contrib.auth.models import User
from home.models import RegisteredUser


class Note(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=25)
    body = models.CharField(max_length=250)
    written_date = models.DateField()
    color = models.CharField(max_length=10)

    def __str__(self):
        return str(self.user_id.username) + ' - ' + str(self.title)
