# Generated by Django 5.1.5 on 2025-01-26 12:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('folder_aplikacji', '0009_alter_osoba_options_alter_osoba_plec'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='osoba',
            options={'ordering': ['nazwisko']},
        ),
    ]
