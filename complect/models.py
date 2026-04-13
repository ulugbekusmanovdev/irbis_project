from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Postupleny(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name="ФИО")
    date_numksu = models.CharField(null=True, blank=True,max_length=200, verbose_name='Год и номер записи в КСУ')
    num_akt = models.CharField(null=True, blank=True,max_length=200, verbose_name='Номер акта индивидуального учета')
    create_date = models.DateTimeField(auto_now=True, verbose_name='Дата')
    num_sop_doc = models.CharField(null=True, blank=True,max_length=200, verbose_name='Номер сопроводительного документа')
    istochnic_c = models.CharField(null=True, blank=True,max_length=200, default='НБОшГУ', verbose_name='Источник комплектования (КОД)')
    date_naimen = models.CharField(null=True, blank=True,max_length=200, verbose_name='Число наименований')
    date_ekzam = models.CharField(null=True, blank=True,max_length=200, verbose_name='Число экземпляров')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='На сумму')
    
    class Meta:
        verbose_name_plural = 'Сведения о поступлении книг в библиотеку'

    def __str__(self):
        return str(self.date_numksu)

class RZN(models.Model):
    title = models.CharField(max_length=200, db_index=True)

    class Meta:
        verbose_name_plural = ' По разделам знаний'

    def __str__(self):
        return self.title

class Raspredeleny(models.Model):
    # post = models.ForeignKey(Postupleny, on_delete=models.CASCADE)  # ОБЯЗАТЕЛЬНО
    category = models.ForeignKey(RZN, verbose_name='По разделам знаний', on_delete=models.CASCADE, null=True)
    books = models.CharField(null=True, blank=True,max_length=200, verbose_name='Книги на баланс')
    broshur = models.CharField(null=True, blank=True,max_length=200, verbose_name='Брошюры')
    journal = models.CharField(null=True, blank=True,max_length=200, verbose_name='Журналы')
    aud_vid = models.CharField(null=True, blank=True,max_length=200, verbose_name='Аудио/Видео')
    carty = models.CharField(null=True, blank=True,max_length=200, verbose_name='Карты')
    noty = models.CharField(null=True, blank=True,max_length=200, verbose_name='Ноты')
    electron_izd = models.CharField(null=True, blank=True,max_length=200, verbose_name='Электронные издания')
    prochy = models.CharField(null=True, blank=True,max_length=200, verbose_name='Прочие')
    russian = models.CharField(null=True, blank=True,max_length=200, verbose_name='русский язык')
    national = models.CharField(null=True, blank=True,max_length=200, verbose_name='национальный язык')
    other = models.CharField(null=True, blank=True,max_length=200, verbose_name='другой язык')
    inv_num = models.CharField(null=True, blank=True,max_length=200, verbose_name='Макс. и мин. инв номера партии')
    bez_periodiki = models.CharField(null=True, blank=True,max_length=200, verbose_name='Всего наименований без периодики')
    all_examp = models.CharField(null=True, blank=True,max_length=200, verbose_name='Всего экземпляров')
    summa = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Всего на сумму')

    class Meta:
        verbose_name_plural = 'Данные распределения партии'

    def __str__(self):
        return str(self.books)