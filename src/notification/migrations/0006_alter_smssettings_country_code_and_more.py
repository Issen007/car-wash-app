# Generated by Django 4.1 on 2022-09-21 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0005_smssettings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smssettings',
            name='country_code',
            field=models.IntegerField(default=46),
        ),
        migrations.AlterField(
            model_name='smssettings',
            name='phonenumber',
            field=models.IntegerField(default=70123456),
        ),
    ]