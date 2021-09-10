from kitchen.models import Combo
from users.models import Profile

from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Dish(models.Model):
    name = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    price = models.FloatField()
    measurement = models.ManyToManyField(Combo, blank=True)
    cost = models.FloatField(null = True)

    def __str__(self):
        return self.name 

    def get_cost(self):
        ingrediants = self.measurement.all()
        print(ingrediants)
        cost = 0
        for ingrediant in ingrediants:
            print(ingrediant)
            cost += ingrediant.cost
        return cost


class Cart(models.Model):
    STATUS_CHOICE = [
        ('O', 'Open'),
        ('P', 'Pending'),
        ('C', 'Closed'),
    ]
    
    status = models.CharField(choices=STATUS_CHOICE, max_length=50, default='O') 
    date_created = models.DateTimeField(auto_now_add=True)
    profile = models.ForeignKey(Profile,on_delete=CASCADE)
    price = models.FloatField() #dont need
    order_number = models.TextField() #dont neews

    def create_cart(self):
        pid = self.profile.id
        pid = str(pid)
        cid = '0'
        order = pid + '-' + cid
        Cart.objects.create(profile= self.profile,price = 0,order_number = order)

    def check_out(self,pk):
        cart =Cart.objects.get(id = pk)
        cart.status = 'P'
        print(self )
        cart.save()
        
        pid = cart.profile.id
        pid = str(pid)
        cid = cart.id 
        cid = cid + 1
        print(cid)
        cid = str(cid)
        order = pid + '-' + cid
        Cart.objects.create(profile= cart.profile,price = 0,order_number = order)
        
    

    def total(self):
        ttl = 0
        for sing in self.singular_set.all():
            ttl += sing.dish.price
        return ttl


class Singular(models.Model):
    dish = models.ForeignKey(Dish, on_delete=CASCADE)
    comments = models.TextField()
    cart = models.ForeignKey(Cart, on_delete=CASCADE)
    def __str__(self):
        return self.dish.name
         





