# Generated by Django 5.1.3 on 2024-11-24 08:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoala', '0006_elev_restdeplata'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='elev',
            options={'ordering': ['nume', 'prenume']},
        ),
    ]