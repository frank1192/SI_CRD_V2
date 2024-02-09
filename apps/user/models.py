from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
     identification = models.PositiveBigIntegerField(unique=True, blank=False, null=False, verbose_name='identification')
    
     def __str__(self):
         return f"{self.id}- {self.identification} | {self.name}"
    
     USERNAME_FIELDS= 'username'
     REQUIRED_FIELDS= ['first_name','identification']
    
     class Meta:
         verbose_name='Usuario'
         verbose_name_plural='Usuarios'
         db_table='USER'
         ordering=['id']