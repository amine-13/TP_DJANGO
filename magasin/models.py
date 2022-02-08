from distutils.command.upload import upload
from django.db import models
from django.conf import settings

from django.urls import reverse

class AbstractMere(models.Model):

    name = models.CharField(max_length=200)
    country = models.CharField(max_length=200, choices=settings.COUNTRIES)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.name

    class Meta:
        abstract = True
        ordering = ['name', ]


class Magasin(AbstractMere):
    pass

    

class MagasinProfile(models.Model):
    
    email = models.EmailField(max_length=255, unique=True)
    phone = models.CharField(max_length=30, unique=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    magasin = models.OneToOneField(Magasin, 
                                    on_delete=models.CASCADE, 
                                    related_name = 'magasin_profile'
                                )

class Produit(AbstractMere):
    price = models.DecimalField(max_digits=10, decimal_places=2)
    magasin = models.ForeignKey(Magasin, on_delete=models.CASCADE, related_name='product_magasin'
                       )