from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,verbose_name='کاربر')
    father_name=models.CharField(max_length=70,verbose_name='نام پدر')
    melicode=models.CharField(max_length=20,verbose_name='کد ملی')
    image=models.ImageField(upload_to='images/profile',null=True,blank=True,verbose_name='عکس')
    phone=models.IntegerField(null=True,blank=True,verbose_name='تلفن')
    adress=models.TextField(blank=True,null=True,verbose_name='آدرس')

    class Meta:
        verbose_name='حساب کاربری'
        verbose_name_plural='حساب های کاربری'
    def __str__(self):
        return f'{self.user}'
