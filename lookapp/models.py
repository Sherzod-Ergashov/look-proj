from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.translation import pgettext_lazy


# Create your models here.
class Type(models.Model):
    objects = None
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name

class Book(models.Model):
    objects = None
    title = models.CharField(max_length=200)
    description = models.TextField()
    isbn = models.CharField(max_length=17)
    cover_picture = models.ImageField(default="default_cover.jpg")
    price = models.DecimalField(max_digits=6, decimal_places=2, default=1000)
    language = models.CharField(max_length=30, default='english')
    type = models.ForeignKey(Type, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.title)

class Auther(models.Model):
    objects = None
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    bio = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

class BookAuthor(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    auther = models.ForeignKey(Auther, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.book.title} by {self.auther.last_name} {self.auther.first_name}"


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
