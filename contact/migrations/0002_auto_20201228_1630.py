# Generated by Django 3.1.4 on 2020-12-28 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('label', '0001_initial'),
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(blank=True, default='', max_length=255, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='firstname',
            field=models.CharField(blank=True, default='', max_length=45, verbose_name='firstname'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to='contact'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='labels',
            field=models.ManyToManyField(blank=True, to='label.Label'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='lastname',
            field=models.CharField(blank=True, default='', max_length=45, verbose_name='lastname'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='nickname',
            field=models.CharField(blank=True, default='', max_length=45, verbose_name='nickname'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='phone'),
        ),
    ]