# Generated by Django 3.1.4 on 2020-12-31 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_contact_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='profile',
            field=models.BooleanField(default=False, verbose_name='profile'),
        ),
    ]
