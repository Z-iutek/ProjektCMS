<<<<<<< HEAD
# Generated by Django 5.0.3 on 2024-04-10 20:00
=======
# Generated by Django 4.0.5 on 2024-04-10 19:10
>>>>>>> 672c87f (Dodanie Tabeli)

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Startstrona', '0008_remove_stanstrony_h1_stanstrony_naglowek_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stanstrony',
            name='Tekst_glowny',
            field=models.TextField(default='Wpisz tekst glowny', max_length=2000),
        ),
    ]
