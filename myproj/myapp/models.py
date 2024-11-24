from django.db import models

# Create your models here.
#hello
class katalog(models.Model):
    phone = models.CharField(max_length = 50, verbose_name="Модель телефона")
    cost = models.IntegerField(verbose_name="Стоимость")
    gb = models.CharField(max_length = 50, verbose_name="Количество памяти")
    camer = models.CharField(max_length = 50, verbose_name="Количество мегапикселей в камере")
    date = models.DateField(auto_now=True, verbose_name="Дата публикации товара")
    img = models.ImageField(upload_to="myapp/static/img", blank=True)
    des = models.CharField(max_length=1000, verbose_name="Описание товара", blank = True)

    def __str__(self):
        return self.phone
    

    def procent(self, a):
        return self.cost * (a/100)
    
class users_log_psw(models.Model):
    log = models.CharField(max_length= 15,verbose_name="Login")
    psw = models.IntegerField(verbose_name="Password")
    name = models.CharField(max_length= 100, verbose_name="Name")
    data = models.DateField(auto_now=True, blank=True)
	
#test commit
