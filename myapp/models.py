from django.db import models

# Create your models here.
class product(models.Model):
    pname = models.CharField(max_length=20 ,null=False)
    pprice = models.IntegerField(null=False)
    pdescription = models.TextField(max_length=255, null = False)
    pimage = models.CharField(max_length=20, null=False)
    pstock = models.IntegerField(null=False)
    def __str__(self):
        return self.pname
