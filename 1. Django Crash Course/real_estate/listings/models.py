from django.db import models

# Create your models here.
# Models are representations of Database schema where we convert database tables to python
# objects so we can interact with the database using Python

class Listing(models.Model): # class will be interpreted as a database table
    title = models.CharField(max_length=150)
    price = models.IntegerField()
    num_bedrooms = models.IntegerField()
    num_bathrooms = models.IntegerField()
    square_footage = models.IntegerField()
    address = models.CharField(max_length=300)
    # image 
    
    def __str__(self):
        return self.title