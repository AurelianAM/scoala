# Generated by Django 5.1.3 on 2024-11-17 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoala', '0003_anscolar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anscolar',
            name='anFinal',
            field=models.IntegerField(default=2025),
        ),
        migrations.AlterField(
            model_name='anscolar',
            name='anStart',
            field=models.IntegerField(default=2024),
        ),
    ]
