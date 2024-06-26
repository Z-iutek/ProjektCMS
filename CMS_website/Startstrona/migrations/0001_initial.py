# Generated by Django 5.0.3 on 2024-04-14 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StanStrony',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kolor_tla', models.CharField(default='Wpisz kolor', max_length=7)),
                ('tytul_strony', models.CharField(default='Wybierz tytuł', max_length=200)),
                ('nazwa', models.CharField(default='Nazwa zapisu', max_length=100)),
                ('Naglowek', models.CharField(default='Wpisz naglowek', max_length=200)),
                ('Tekst_glowny', models.TextField(default='Wpisz tekst glowny', max_length=2000)),
                ('Stopka', models.CharField(default='Wpisz stopke', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
            ],
        ),
    ]
