# Generated by Django 5.1.2 on 2025-01-19 13:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('folder_aplikacji', '0003_stanowisko_alter_person_pseudonim_osoba'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='osoba',
            options={'ordering': ['-nazwisko']},
        ),
    ]
