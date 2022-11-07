from django.db import models
import string
import random

def generate_unique_code():
    length = 6
    while True:
        code = ''.join(random.choices(string.ascii_lowercase, k=length))
        if Store.objects.filter(code=code).count() == 0:
            break
    return code



# Create your models here.
# TODO: Build out data model
# automatically an id field on every
class Store(models.Model):
    code = models.CharField(max_length=8, default="", unique=True)

