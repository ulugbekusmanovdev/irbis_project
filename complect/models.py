from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Postupleny(models.Model):
    date_numksu = models.CharField(null=True, blank=True,max_length=200, verbose_name='Год и номер записи в КСУ')
    num_akt = models.CharField(null=True, blank=True,max_length=200, verbose_name='Номер акта индивидуального учета')
    create_date = models.DateTimeField(auto_now=True, verbose_name='Дата')
    num_sop_doc = models.CharField(null=True, blank=True,max_length=200, verbose_name='Номер сопроводительного документа')
    istochnic_c = models.CharField(null=True, blank=True,max_length=200, verbose_name='Источник комплектования (КОД)')
    num_order = models.CharField(null=True, blank=True,max_length=200, verbose_name='Номер заказа')
    date_naimen = models.CharField(null=True, blank=True,max_length=200, verbose_name='Число наименований')
    date_ekzam = models.CharField(null=True, blank=True,max_length=200, verbose_name='Число экземпляров')
    price = models.CharField(null=True, blank=True,max_length=200, verbose_name='На сумму')
    cost = models.CharField(null=True, blank=True,max_length=200, verbose_name='Платно/бесплатно')
    nds = models.CharField(null=True, blank=True,max_length=200, verbose_name='В том числе - НДС')

    def __str__(self):
        return self.date_numksu
    
LEVEL_WORK = [
    ("1", "ПК-Создание записи"),
    ("2", "РЗ - Размещение заказа"),
    ("3", "ИЗ - Исполнение заказа"),
    ("4", "КТ - Каталогизация"),
    ("5", "С - Систематизация"),
    ("6", "ДК - Докомплектование"),
    ("7", "КР - Корректура"),
    ("8", "ВБ - Выбытие"),
]    

class Levelwork(models.Model):
    levelwork = models.CharField(max_length=2, choices=LEVEL_WORK, default="1")
    create_date = models.DateTimeField(auto_now=True, verbose_name='Дата')
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.levelwork

class Zapisksu(models.Model):
    sv_postupleni = models.ForeignKey(Postupleny, on_delete=models.CASCADE, null=True, blank=True,verbose_name='Сведения о поступлении книг в библиотеку')
    sv_zamene = models.CharField(null=True, blank=True,max_length=200, verbose_name=' Сведения о замене утерянных книг')
    levelwork = models.ForeignKey(Levelwork, on_delete=models.CASCADE, null=True, blank=True,verbose_name='Этап работы, дата, ФИО')

    def __str__(self):
        return self.sv_postupleni
