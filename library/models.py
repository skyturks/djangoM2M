from django.db import models
from django.contrib.auth.models import User as DjangoUser
# Create your models here.


class Library(models.Model):
    title = models.CharField(max_length=100, null=True)
    user = models.ManyToManyField(DjangoUser, db_table='user_library', related_name='library_id')