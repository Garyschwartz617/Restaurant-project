from finance.models import Bill
from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Ingrediant(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class Measurement(models.Model):
    name = models.CharField(max_length=300)
    amount_per_kilo = models.FloatField()

    def __str__(self):
        return self.name

class Transaction(models.Model):
    measurement = models.ForeignKey(Measurement, on_delete=CASCADE)
    ingrediant = models.ForeignKey(Ingrediant, on_delete=CASCADE)
    cost = models.IntegerField()
    bill = models.ForeignKey(Bill, on_delete=CASCADE,null = True,blank=True)

    def __str__(self):
        return self.ingrediant.name 

class Combo(models.Model):
    measurement = models.ForeignKey(Measurement, on_delete=CASCADE)
    ingrediant = models.ForeignKey(Ingrediant, on_delete=CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    cost = models.IntegerField()
    # dish = models.ForeignKey('service.Dish', on_delete=CASCADE)

    def __str__(self):
        return f'{self.measurement.name} {self.ingrediant.name}'

    def cost_per(self):
        tran =Transaction.objects.filter(ingrediant= self.ingrediant).last()
        orig_cost = tran.cost
        orig_measu = tran.measurement.amount_per_kilo
        measur = self.measurement.amount_per_kilo
        cost = orig_cost / orig_measu
        cost = cost * measur
        return cost