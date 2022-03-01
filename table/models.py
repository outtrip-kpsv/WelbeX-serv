from django.db import models


# Create your models here.
class TableRows(models.Model):
    date = models.DateField(verbose_name='Дата')
    name = models.CharField(max_length=200, verbose_name='Название')
    quantity = models.IntegerField(verbose_name='Количество')
    distance = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Расстояние')
