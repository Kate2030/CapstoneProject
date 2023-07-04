from django.db import models
from django.utils.timezone import now


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
class CarMake(models.Model):
    Name = models.CharField(null=False, max_length=25)
    Description = models.CharField(null=False, max_length=250)
   
# - Any other fields you would like to include in car make model
def __str__(self):
    return self.name


# <HINT> Create a Car Model model `class CarModel(models.Model):`:
class CarModel(models.Model):
     Van = 'Van'
     Suv = 'Suv'
     Combi = 'Combi'
     Hatchback = 'Hatchback'
     Sedan = 'Sedan'
     Sport = 'Sport'
     
     Car_choices = [(Van,'Van'), (Suv,'Suv'),(Combi,'Combi'),(Hatchback,'Hatchback'),(Sedan,'Sedan'),
     (Sport,'Sport')]

def __str__(self):
    return self.name

# <HINT> Create a plain Python class `CarDealer` to hold dealer data

# <HINT> Create a plain Python class `DealerReview` to hold review data
