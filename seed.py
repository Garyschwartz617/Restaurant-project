import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Restaurant.settings')
django.setup()


from users.models import *
from finance.models import *
from kitchen.models import *
from service.models import *

# FINANCE
# Tipes 
s = ('Rent','Produce', 'Electricity','Water','Food')

for a in s:
    Tipe.objects.get_or_create(name= a)

# Bills
Bill.objects.get_or_create(name='Chashmol',cost=1500,tipe=Tipe.objects.get(id=3))    
Bill.objects.get_or_create(name='Food Deleivery Co.',cost=10000,tipe=Tipe.objects.get(id=5))    
Bill.objects.get_or_create(name='Mei Shemesh',cost=1300,tipe=Tipe.objects.get(id=4))    
Bill.objects.get_or_create(name='Rent',cost=7000,tipe=Tipe.objects.get(id=1))    
Bill.objects.get_or_create(name='Produce Delivery Co,',cost=5000,tipe=Tipe.objects.get(id=2))    

# KITCHEN
# Ingrediants 
s = ('Salt','Pepper', 'Paprika','Cumin','Spicy Spice', 'Rice','lentils','Lettuce','Corn','Cucumbers','Peppers','Pickles', 'Regular Shell', 'Whole Wheat Shell','Regular Soft Tortilla','Whole Wheat Soft Tortilla','Meat','Fake Meat','Fish Ground Meat' )

for a in s:
    Ingrediant.objects.get_or_create(name= a)
# Measurements
s = (('10 KiloGrams',10), ('5 KiloGrams',5),('3 KiloGrams', 3), ('1.3 KiloGram', 1.3), ('1 KiloGram', 1),('700 Grams', .7),('650 Grams', .65),('600 Grams', .6),('500 Grams', .5),('300 Grams', .3),('150 Grams', .15),('130 Grams', .13),('100 Grams', .1),('65 Grams', .065),('60 Grams', .06),('50 Grams', .05),('30 Grams',.03),('15 Grams', .015),('10 Grams', .01),('5 Grams', .005),('10,000 Count',10000),('5,000 Count', 5000),('1,000 Count', 1000),('13 Count', 13), ('6 Count', 6), ('3 Count',3),('1 Count',1),('165 Grams', .165))

for a in s:
    Measurement.objects.get_or_create(name= a[0],amount_per_kilo= a[1])

# Transactions

s = [[Measurement.objects.get(id = 1),Ingrediant.objects.get(name= 'Salt'),70, Bill.objects.get(id =2)],[Measurement.objects.get(id = 2),Ingrediant.objects.get(name= 'Pepper'),40, Bill.objects.get(id =2)], [Measurement.objects.get(id = 2),Ingrediant.objects.get(name= 'Paprika'),45, Bill.objects.get(id =2)],[Measurement.objects.get(id = 2),Ingrediant.objects.get(name= 'Cumin'),42, Bill.objects.get(id =2)],[Measurement.objects.get(id = 2),Ingrediant.objects.get(name= 'Spicy Spice'),55, Bill.objects.get(id =2)], [Measurement.objects.get(id = 1),Ingrediant.objects.get(name= 'Rice'),50, Bill.objects.get(id =2)],[Measurement.objects.get(id = 1),Ingrediant.objects.get(name= 'lentils'),60, Bill.objects.get(id =2)],[Measurement.objects.get(id = 1),Ingrediant.objects.get(name= 'Lettuce'),100, Bill.objects.get(id =5)],[Measurement.objects.get(id = 3),Ingrediant.objects.get(name= 'Corn'),20, Bill.objects.get(id =5)],[Measurement.objects.get(id = 2),Ingrediant.objects.get(name= 'Cucumbers'),30, Bill.objects.get(id =5)],[Measurement.objects.get(id = 3),Ingrediant.objects.get(name= 'Peppers'),15, Bill.objects.get(id =5)],[Measurement.objects.get(id = 2),Ingrediant.objects.get(name= 'Pickles'),35, Bill.objects.get(id =5)], [Measurement.objects.get(name= '10,000 Count'),Ingrediant.objects.get(name= 'Regular Shell'),1000, Bill.objects.get(id =2)], [Measurement.objects.get(name= '5,000 Count'),Ingrediant.objects.get(name= 'Whole Wheat Shell'),550, Bill.objects.get(id =2)],[Measurement.objects.get(name= '5,000 Count'),Ingrediant.objects.get(name= 'Regular Soft Tortilla'),400, Bill.objects.get(id =2)],[Measurement.objects.get(name= '1,000 Count'),Ingrediant.objects.get(name= 'Whole Wheat Soft Tortilla'),100, Bill.objects.get(id =2)],[Measurement.objects.get(id = 1),Ingrediant.objects.get(name= 'Meat'),300, Bill.objects.get(id =2)],[Measurement.objects.get(id = 1),Ingrediant.objects.get(name= 'Fake Meat'),300, Bill.objects.get(id =2)],[Measurement.objects.get(id = 1),Ingrediant.objects.get(name= 'Fish Ground Meat'),300, Bill.objects.get(id =2)] ]

for a in s:
    Transaction.objects.get_or_create(measurement= a[0],ingrediant= a[1], cost=a[2],bill=a[3])

# # combo's

s = [[Measurement.objects.get(name= '5 Grams'),Ingrediant.objects.get(name= 'Salt')],[Measurement.objects.get(name= '5 Grams'),Ingrediant.objects.get(name= 'Pepper')], [Measurement.objects.get(name= '5 Grams'),Ingrediant.objects.get(name= 'Paprika')],[Measurement.objects.get(name= '5 Grams'),Ingrediant.objects.get(name= 'Cumin')],[Measurement.objects.get(name= '5 Grams'),Ingrediant.objects.get(name= 'Spicy Spice')], [Measurement.objects.get(name= '50 Grams'),Ingrediant.objects.get(name= 'Rice')],[Measurement.objects.get(name= '50 Grams'),Ingrediant.objects.get(name= 'lentils')],[Measurement.objects.get(name= '50 Grams'),Ingrediant.objects.get(name= 'Lettuce')],[Measurement.objects.get(name= '10 Grams'),Ingrediant.objects.get(name= 'Corn')],[Measurement.objects.get(name= '10 Grams'),Ingrediant.objects.get(name= 'Cucumbers')],[Measurement.objects.get(name= '10 Grams'),Ingrediant.objects.get(name= 'Peppers')],[Measurement.objects.get(name= '10 Grams'),Ingrediant.objects.get(name= 'Pickles')], [Measurement.objects.get(name= '1 Count'),Ingrediant.objects.get(name= 'Regular Shell')], [Measurement.objects.get(name= '1 Count'),Ingrediant.objects.get(name= 'Whole Wheat Shell'),],[Measurement.objects.get(name= '1 Count'),Ingrediant.objects.get(name= 'Regular Soft Tortilla')],[Measurement.objects.get(name= '1 Count'),Ingrediant.objects.get(name= 'Whole Wheat Soft Tortilla')],[Measurement.objects.get(name= '50 Grams'),Ingrediant.objects.get(name= 'Meat')],[Measurement.objects.get(name= '50 Grams'),Ingrediant.objects.get(name= 'Fake Meat')],[Measurement.objects.get(name= '50 Grams'),Ingrediant.objects.get(name= 'Fish Ground Meat')],

[Measurement.objects.get(name= '15 Grams'),Ingrediant.objects.get(name= 'Salt')],[Measurement.objects.get(name= '15 Grams'),Ingrediant.objects.get(name= 'Pepper')], [Measurement.objects.get(name= '15 Grams'),Ingrediant.objects.get(name= 'Paprika')],[Measurement.objects.get(name= '15 Grams'),Ingrediant.objects.get(name= 'Cumin')],[Measurement.objects.get(name= '15 Grams'),Ingrediant.objects.get(name= 'Spicy Spice')], [Measurement.objects.get(name= '150 Grams'),Ingrediant.objects.get(name= 'Rice')],[Measurement.objects.get(name= '150 Grams'),Ingrediant.objects.get(name= 'lentils')],[Measurement.objects.get(name= '150 Grams'),Ingrediant.objects.get(name= 'Lettuce')],[Measurement.objects.get(name= '30 Grams'),Ingrediant.objects.get(name= 'Corn')],[Measurement.objects.get(name= '30 Grams'),Ingrediant.objects.get(name= 'Cucumbers')],[Measurement.objects.get(name= '30 Grams'),Ingrediant.objects.get(name= 'Peppers')],[Measurement.objects.get(name= '30 Grams'),Ingrediant.objects.get(name= 'Pickles')], [Measurement.objects.get(name= '3 Count'),Ingrediant.objects.get(name= 'Regular Shell')], [Measurement.objects.get(name= '3 Count'),Ingrediant.objects.get(name= 'Whole Wheat Shell'),],[Measurement.objects.get(name= '3 Count'),Ingrediant.objects.get(name= 'Regular Soft Tortilla')],[Measurement.objects.get(name= '3 Count'),Ingrediant.objects.get(name= 'Whole Wheat Soft Tortilla')],[Measurement.objects.get(name= '150 Grams'),Ingrediant.objects.get(name= 'Meat')],[Measurement.objects.get(name= '150 Grams'),Ingrediant.objects.get(name= 'Fake Meat')],[Measurement.objects.get(name= '150 Grams'),Ingrediant.objects.get(name= 'Fish Ground Meat')],

[Measurement.objects.get(name= '30 Grams'),Ingrediant.objects.get(name= 'Salt')],[Measurement.objects.get(name= '30 Grams'),Ingrediant.objects.get(name= 'Pepper')], [Measurement.objects.get(name= '30 Grams'),Ingrediant.objects.get(name= 'Paprika')],[Measurement.objects.get(name= '30 Grams'),Ingrediant.objects.get(name= 'Cumin')],[Measurement.objects.get(name= '30 Grams'),Ingrediant.objects.get(name= 'Spicy Spice')],[Measurement.objects.get(name= '300 Grams'),Ingrediant.objects.get(name= 'Rice')],[Measurement.objects.get(name= '300 Grams'),Ingrediant.objects.get(name= 'lentils')],[Measurement.objects.get(name= '300 Grams'),Ingrediant.objects.get(name= 'Lettuce')],[Measurement.objects.get(name= '60 Grams'),Ingrediant.objects.get(name= 'Corn')],[Measurement.objects.get(name= '60 Grams'),Ingrediant.objects.get(name= 'Cucumbers')],[Measurement.objects.get(name= '60 Grams'),Ingrediant.objects.get(name= 'Peppers')],[Measurement.objects.get(name= '60 Grams'),Ingrediant.objects.get(name= 'Pickles')], [Measurement.objects.get(name= '6 Count'),Ingrediant.objects.get(name= 'Regular Shell')], [Measurement.objects.get(name= '6 Count'),Ingrediant.objects.get(name= 'Whole Wheat Shell'),],[Measurement.objects.get(name= '6 Count'),Ingrediant.objects.get(name= 'Regular Soft Tortilla')],[Measurement.objects.get(name= '6 Count'),Ingrediant.objects.get(name= 'Whole Wheat Soft Tortilla')],[Measurement.objects.get(name= '300 Grams'),Ingrediant.objects.get(name= 'Meat')],[Measurement.objects.get(name= '300 Grams'),Ingrediant.objects.get(name= 'Fake Meat')],[Measurement.objects.get(name= '300 Grams'),Ingrediant.objects.get(name= 'Fish Ground Meat')],

[Measurement.objects.get(name= '65 Grams'),Ingrediant.objects.get(name= 'Salt')],[Measurement.objects.get(name= '65 Grams'),Ingrediant.objects.get(name= 'Pepper')], [Measurement.objects.get(name= '65 Grams'),Ingrediant.objects.get(name= 'Paprika')],[Measurement.objects.get(name= '65 Grams'),Ingrediant.objects.get(name= 'Cumin')],[Measurement.objects.get(name= '65 Grams'),Ingrediant.objects.get(name= 'Spicy Spice')], [Measurement.objects.get(name= '165 Grams'),Ingrediant.objects.get(name= 'Rice')],[Measurement.objects.get(name= '165 Grams'),Ingrediant.objects.get(name= 'lentils')],[Measurement.objects.get(name= '165 Grams'),Ingrediant.objects.get(name= 'Lettuce')],[Measurement.objects.get(name= '130 Grams'),Ingrediant.objects.get(name= 'Corn')],[Measurement.objects.get(name= '130 Grams'),Ingrediant.objects.get(name= 'Cucumbers')],[Measurement.objects.get(name= '130 Grams'),Ingrediant.objects.get(name= 'Peppers')],[Measurement.objects.get(name= '130 Grams'),Ingrediant.objects.get(name= 'Pickles')], [Measurement.objects.get(name= '13 Count'),Ingrediant.objects.get(name= 'Regular Shell')], [Measurement.objects.get(name= '13 Count'),Ingrediant.objects.get(name= 'Whole Wheat Shell'),],[Measurement.objects.get(name= '13 Count'),Ingrediant.objects.get(name= 'Regular Soft Tortilla')],[Measurement.objects.get(name= '13 Count'),Ingrediant.objects.get(name= 'Whole Wheat Soft Tortilla')],[Measurement.objects.get(name= '165 Grams'),Ingrediant.objects.get(name= 'Meat')],[Measurement.objects.get(name= '165 Grams'),Ingrediant.objects.get(name= 'Fake Meat')],[Measurement.objects.get(name= '165 Grams'),Ingrediant.objects.get(name= 'Fish Ground Meat')],

]

# # [Measurement.objects.get(id = 10),Ingrediant.objects.get(name= 'Salt')],[Measurement.objects.get(id = 10),Ingrediant.objects.get(name= 'Pepper')], [Measurement.objects.get(id = 10),Ingrediant.objects.get(name= 'Paprika')],[Measurement.objects.get(id = 10),Ingrediant.objects.get(name= 'Cumin')],[Measurement.objects.get(id = 10),Ingrediant.objects.get(name= 'Spicy Spice')], [Measurement.objects.get(id = 8),Ingrediant.objects.get(name= 'Rice')],[Measurement.objects.get(id = 8),Ingrediant.objects.get(name= 'lentils')],[Measurement.objects.get(id = 8),Ingrediant.objects.get(name= 'Lettuce')],[Measurement.objects.get(id = 9),Ingrediant.objects.get(name= 'Corn')],[Measurement.objects.get(id = 9),Ingrediant.objects.get(name= 'Cucumbers')],[Measurement.objects.get(id = 9),Ingrediant.objects.get(name= 'Peppers')],[Measurement.objects.get(id = 9),Ingrediant.objects.get(name= 'Pickles')], [Measurement.objects.get(id = 16),Ingrediant.objects.get(name= 'Regular Shell')], [Measurement.objects.get(id = 16),Ingrediant.objects.get(name= 'Whole Wheat Shell'),],[Measurement.objects.get(id = 16),Ingrediant.objects.get(name= 'Regular Soft Tortilla')],[Measurement.objects.get(id = 16),Ingrediant.objects.get(name= 'Whole Wheat Soft Tortilla')],[Measurement.objects.get(id = 8),Ingrediant.objects.get(name= 'Meat')],[Measurement.objects.get(id = 8),Ingrediant.objects.get(name= 'Fake Meat')],[Measurement.objects.get(id = 8),Ingrediant.objects.get(name= 'Fish Ground Meat')] ]
# print('hello')




for a in s:
    print('hello')
    tran =Transaction.objects.filter(ingrediant= a[1]).last()
    orig_cost = tran.cost
    orig_measu = tran.measurement.amount_per_kilo
    measur = a[0].amount_per_kilo
    cost = orig_cost / orig_measu
    cost = cost * measur

    combo = Combo.objects.get_or_create(measurement= a[0],ingrediant= a[1],cost = cost)
