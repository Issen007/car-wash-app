# Generated by Django 4.1 on 2022-09-06 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_work_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='started',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='work',
            name='status',
            field=models.CharField(blank=True, default='', max_length=16),
        ),
    ]
