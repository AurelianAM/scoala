# Generated by Django 5.1.3 on 2024-11-23 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestiune', '0002_alter_fondrate_clasa'),
    ]

    operations = [
        migrations.AddField(
            model_name='fondrate',
            name='applied',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='fondrate',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
