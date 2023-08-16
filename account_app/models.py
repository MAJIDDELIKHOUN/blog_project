from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    father_name=models.CharField(max_length=70)
    melicode=models.CharField(max_length=20)
    image=models.ImageField(upload_to='images/profile',null=True,blank=True)
    phone=models.IntegerField(null=True,blank=True)
    adress=models.TextField(blank=True,null=True)

    def __str__(self):
        return f'{self.user}'
