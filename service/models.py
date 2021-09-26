from kitchen.models import Combo
from users.models import Profile

from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

# class Course(models.Model):
#     name = models.CharField(max_length=200)
#     def __str__(self):
#         return self.name 


class Dish(models.Model):
    name = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    price = models.FloatField()
    measurement = models.ManyToManyField(Combo, blank=True)
    cost = models.FloatField(null = True)
    # course = models.ForeignKey(Course, on_delete=CASCADE)
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
    profile = models.ForeignKey(Profile,on_delete=CASCADE,related_name='cart_profile')
    cust = models.ForeignKey(Profile,on_delete=CASCADE,related_name='cart_cust',null=True,blank=True)
    customer = models.CharField(max_length=100,null=True,blank=True)
    # price = models.FloatField() #dont need
    # order_number = models.TextField() #dont neews

    def create_cart(self):
        Cart.objects.create(profile= self.profile)

    def check_out(self,pk):
        cart =Cart.objects.get(id = pk)
        cart.status = 'P'
        cart.save()
            

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
         
    def get_form(self):
        from .forms import EditSingular2Form
        return EditSingular2Form(instance = self) # iniital = {'comments': self.comments}