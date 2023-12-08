from django.db import models
from datetime import datetime


class Admin(models.Model):
    Id=models.AutoField(primary_key=True,auto_created=True,unique=True,blank=True,null=False,verbose_name="Admin")
    Username = models.CharField(max_length=100,null=False, blank=True)
    Email = models.CharField(max_length=100,unique=True,null=False,blank=True)
    Password = models.CharField(max_length=8, null=False, blank=True)
    Token = models.TextField( blank=True, null=False,default="")
    def __str__(self):
        return '{}'.format(self.Username)
    
class Relay(models.Model):
    Id=models.AutoField(primary_key=True,auto_created=True,unique=True,blank=True,null=False,verbose_name="Relay")
    Value= models.BooleanField(default=False)

    def __str__(self):
        return 'Relay:({}) {}'.format(self.Id,self.Value)
    
class Data(models.Model):
    Id=models.AutoField(primary_key=True,auto_created=True,unique=True,blank=True,null=False,verbose_name="Relay")
    Tension= models.FloatField(default=0)
    Courant= models.FloatField(default=0)
    Puissance= models.FloatField(default=0)
    Energie= models.FloatField(default=0)
    Price= models.FloatField(default=0)
    Temps= models.DateTimeField(default=datetime.now())

    def __str__(self):
        return '{} | Tension: ({}) | Courant: ({}) | Puissance: ({}) | Energie: ({}) | Price: ({}) TND'.format(self.Tension,self.Courant,self.Puissance,self.Energie,self.Price)



