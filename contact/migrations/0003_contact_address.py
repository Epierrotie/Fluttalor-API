# Generated by Django 3.1.2 on 2020-12-30 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_auto_20201228_1630'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='address',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='address'),
        ),
    ]
