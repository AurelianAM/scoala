# Generated by Django 5.1.3 on 2024-11-23 11:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestiune', '0004_rename_applied_fondrate_is_applied_and_more'),
        ('scoala', '0006_elev_restdeplata'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Incasari',
            new_name='Incasare',
        ),
    ]
