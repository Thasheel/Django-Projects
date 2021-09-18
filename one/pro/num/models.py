from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class phone(models.Model):
    phone_no = models.CharField(max_length=10)
    user_id = models.OneToOneField(User, on_delete=models.CASCADE,)#here is a related_name to specify id

    def __str__(self):
        return self.phone_no  # to get typed items
