from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


# Create your models here.


class Kasbiy_Standart(models.Model):
    soha = models.TextField()

    def __str__(self):
        return self.soha


class Kasbiy_Standart_Atamalari(models.Model):
    atama = models.CharField(max_length=50)
    izoh = models.CharField(max_length=300)

    def __str__(self):
        return f"{self.atama} - {self.izoh}"


class Kasbiy_Standart_Huquqiy_Hujjat(models.Model):
    hujjat = models.TextField()

    def __str__(self):
        return self.hujjat



class Category(MPTTModel):
    name = models.CharField(max_length=100)
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children'
    )

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name
