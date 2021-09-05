from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.


class Tipe(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name

class Bill(models.Model):
    name = models.CharField(max_length=300)
    cost = models.IntegerField()
    tipe = models.ForeignKey(Tipe, on_delete=CASCADE)
    pdf = models.ImageField(upload_to='posts/', null=True,blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.tipe.name}: {self.name} '
