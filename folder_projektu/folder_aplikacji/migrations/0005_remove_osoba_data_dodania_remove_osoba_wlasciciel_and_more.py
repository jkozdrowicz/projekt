# Generated by Django 5.1.5 on 2025-01-19 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('folder_aplikacji', '0004_alter_osoba_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='osoba',
            name='data_dodania',
        ),
        migrations.RemoveField(
            model_name='osoba',
            name='wlasciciel',
        ),
        migrations.AlterField(
            model_name='osoba',
            name='plec',
            field=models.CharField(choices=[('K', 'Kobieta'), ('M', 'Męzczyzna'), ('I', 'Inna')], default='I', max_length=1),
        ),
    ]
