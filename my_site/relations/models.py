from django.db import models

# Create your models here.

#example for 1VS1 relations

class Female (models.Model):
    name_female = models.CharField(max_length=50 , null=True)
    def __str__(self):
        return self.name_female


class Male (models.Model):
    name_male =models.CharField(max_length=50, null=True) 
    girl = models.OneToOneField(Female , on_delete=models.CASCADE)   #one to one relation

    def __str__(self):
        return self.name_male


#example for one to many relations (supermarket basket)

class Product (models.Model):
    title = models.CharField(max_length=50 , null=True)
    def __str__(self):
        return self.title


class User(models.Model):
    name = models.CharField(max_length=50 , null=True)
    products = models.ForeignKey(Product, on_delete=models.CASCADE)  
    #one to many relations
    #write here because user is one and product in many
    def __str__(self):
        return self.name
    


#many to many (relation between youtuber and videos)
class Video (models.Model):
    title = models.CharField(max_length=50 , null=True)
    def __str__(self):
        return self.title
    
class Youtuber (models.Model):
    name = models.CharField(max_length=50 , null=True)
    watch = models.ManyToManyField(Video , null=True)  #many to many relation

    def __str__(self):
        return self.name