# Generated by Django 5.1.3 on 2024-11-17 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoala', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='elev',
            name='restDePlata',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=7),
        ),
    ]
