# Generated by Django 5.1.3 on 2024-11-23 10:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestiune', '0003_fondrate_applied_alter_fondrate_is_active'),
        ('scoala', '0006_elev_restdeplata'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fondrate',
            old_name='applied',
            new_name='is_applied',
        ),
        migrations.AlterField(
            model_name='fondrate',
            name='clasa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scoala.clasa'),
        ),
        migrations.CreateModel(
            name='Incasari',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('suma', models.DecimalField(decimal_places=2, default=0, max_digits=7)),
                ('created', models.DateTimeField(auto_now=True)),
                ('is_applied', models.BooleanField(default=False)),
                ('elev', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='scoala.elev')),
            ],
        ),
    ]
