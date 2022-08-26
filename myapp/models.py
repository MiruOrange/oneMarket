from django.db import models

# Create your models here.
class customer(models.Model):
    name = models.CharField(max_length=20, null=False)
    phone = models.CharField(max_length = 10, null=False)
    email = models.EmailField(max_length=50, null=False)
    address = models.CharField(max_length=50, null=False)
    message = models.CharField(max_length=200, null=False)
    itemAmount = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name
