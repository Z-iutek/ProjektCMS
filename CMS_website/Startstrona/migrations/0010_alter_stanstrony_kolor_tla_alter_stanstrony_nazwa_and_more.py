# Generated by Django 5.0.3 on 2024-04-14 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Startstrona', '0009_alter_stanstrony_tekst_glowny'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stanstrony',
            name='kolor_tla',
            field=models.CharField(default='Wpisz kolor', max_length=7),
        ),
        migrations.AlterField(
            model_name='stanstrony',
            name='nazwa',
            field=models.CharField(default='Nazwa zapisu', max_length=100),
        ),
        migrations.AlterField(
            model_name='stanstrony',
            name='tytul_strony',
            field=models.CharField(default='Wybierz tytuł', max_length=200),
        ),
    ]