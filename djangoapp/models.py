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
class CarDealer:
    def_init_(self,address,city,full_name,id,long,short_name,st,state,zip):
    self.address = address # Dealer Address
    self.city = city # Dealer City
    self.full_name = full_name # Dealer Fullname
    self.id=id #Dealer ID
    self.lat=lat # Location lat
    self.long=long # Location long
    self.short_name=short_name # Dealer Shortname
    self.st=st # Dealer State
    self.zip=zip #Zip
    self.idx=0 
def_str_(self):
    return self.fullname 

# <HINT> Create a plain Python class `DealerReview` to hold review data
class DealerReview:
   def_init_(self,name,dealership,id,review,purchase, purchase_date, year, car_make, car_model,):
    self.name = name
    self.dealership = dealership
    self.id = id
    self.review= review
    self.purchase = purchase
    self.purchase_date = purchase_date
    self.review = review
    self.short_name=short_name # Dealer Shortname
  
def_str_(self):
    return "DEALER REVIEW:"+ self.review