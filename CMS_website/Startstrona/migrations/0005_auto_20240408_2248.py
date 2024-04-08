from django.db import migrations

def ustaw_domyslne_nazwy(apps, schema_editor):
    StanStrony = apps.get_model('Startstrona', 'StanStrony')
    for idx, stan in enumerate(StanStrony.objects.all(), start=1):
        stan.nazwa = f'Domyślna nazwa {idx}'
        stan.save()

class Migration(migrations.Migration):

    dependencies = [
        ('Startstrona', '0004_alter_stanstrony_nazwa'),
    ]

    operations = [
        migrations.RunPython(ustaw_domyslne_nazwy),
    ]