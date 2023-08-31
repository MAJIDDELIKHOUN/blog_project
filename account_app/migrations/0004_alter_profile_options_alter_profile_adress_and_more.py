# Generated by Django 4.2.4 on 2023-08-30 13:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account_app', '0003_profile_adress_profile_phone'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'حساب کاربری', 'verbose_name_plural': 'حساب های کاربری'},
        ),
        migrations.AlterField(
            model_name='profile',
            name='adress',
            field=models.TextField(blank=True, null=True, verbose_name='آدرس'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='father_name',
            field=models.CharField(max_length=70, verbose_name='نام پدر'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/profile', verbose_name='عکس'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='melicode',
            field=models.CharField(max_length=20, verbose_name='کد ملی'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.IntegerField(blank=True, null=True, verbose_name='تلفن'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر'),
        ),
    ]
