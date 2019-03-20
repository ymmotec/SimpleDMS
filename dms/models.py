from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(verbose_name='Kategoria', max_length=50)
    description = models.TextField('Opis', max_length=500)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Kategorie'



class Department(models.Model):
    '''Department of the factory'''
    name = models.CharField(verbose_name='Nazwa działu', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Działy'


class Product(models.Model):
    '''Product'''
    name = models.CharField(verbose_name='Nazwa produktu', max_length=150)
    customer_number = models.IntegerField(verbose_name='Numer produktu')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Produkty'


class Document(models.Model):
    '''Published document'''
    title = models.CharField(verbose_name='Tytuł dokumentu', max_length=300)
    document_number = models.CharField(verbose_name="Numer dokumentu/procedury", max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)
    department = models.ManyToManyField(Department)

    def __str__(self):
        return f"{self.document_number} - {self.title}"
