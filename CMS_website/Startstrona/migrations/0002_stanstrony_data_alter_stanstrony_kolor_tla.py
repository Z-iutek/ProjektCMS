# Generated by Django 5.0.3 on 2024-04-14 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Startstrona', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stanstrony',
            name='Data',
            field=models.CharField(default='YEAR-MM-DD', max_length=10),
        ),
        migrations.AlterField(
            model_name='stanstrony',
            name='kolor_tla',
            field=models.CharField(default='Wpisz kolor', max_length=12),
        ),
    ]
