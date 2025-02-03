from django.db import models

from datetime import datetime #used with create to get time



class Product(models.Model):

    options = [
        ('phone','phone'),
        ('computer','computer'),
        ('ahmed','ahmed'),
    ]       #chioces for category field 


    name = models.CharField(max_length=50 )
    content = models.TextField()
    price = models.DecimalField(max_digits=5 , decimal_places=2)
    image = models.ImageField(upload_to= 'photos/%y/%m/%d') 
    #to make each photo in a folder depent on history of uplaod
    active = models.BooleanField(default=True)
    category = models.CharField(max_length=50 , choices= options ,null=True ,blank=True)  

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'product '   #to change model name in admin page
        ordering = ['name']  #order objects in database based on name   



class Test (models.Model):
    date = models.DateField()
    time = models.TimeField(null=True)
    created = models.DateTimeField(default=datetime.now)  #used datatime lib
        #both date and time