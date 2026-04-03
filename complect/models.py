from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Postupleny(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    date_numksu = models.CharField(null=True, blank=True,max_length=200, verbose_name='Год и номер записи в КСУ')
    num_akt = models.CharField(null=True, blank=True,max_length=200, verbose_name='Номер акта индивидуального учета')
    create_date = models.DateTimeField(auto_now=True, verbose_name='Дата')
    num_sop_doc = models.CharField(null=True, blank=True,max_length=200, verbose_name='Номер сопроводительного документа')
    istochnic_c = models.CharField(null=True, blank=True,max_length=200, verbose_name='Источник комплектования (КОД)')
    date_naimen = models.CharField(null=True, blank=True,max_length=200, verbose_name='Число наименований')
    date_ekzam = models.CharField(null=True, blank=True,max_length=200, verbose_name='Число экземпляров')
    price = models.CharField(null=True, blank=True,max_length=200, verbose_name='На сумму')
    

    def __str__(self):
        return self.date_numksu
