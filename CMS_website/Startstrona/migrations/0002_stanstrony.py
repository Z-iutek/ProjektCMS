# Generated by Django 5.0.3 on 2024-04-08 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Startstrona', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StanStrony',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kolor_tla', models.CharField(default='#FFFFFF', max_length=7)),
                ('tytul_strony', models.CharField(default='Tytuł domyślny', max_length=200)),
            ],
        ),
    ]
