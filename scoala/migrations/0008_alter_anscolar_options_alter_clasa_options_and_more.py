# Generated by Django 5.1.3 on 2024-11-30 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoala', '0007_alter_elev_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='anscolar',
            options={'verbose_name_plural': 'Ani Scolari'},
        ),
        migrations.AlterModelOptions(
            name='clasa',
            options={'verbose_name_plural': 'Clase'},
        ),
        migrations.AlterModelOptions(
            name='elev',
            options={'ordering': ['nume', 'prenume'], 'verbose_name_plural': 'Elevi'},
        ),
        migrations.AlterModelOptions(
            name='profesor',
            options={'verbose_name_plural': 'Profesori'},
        ),
        migrations.AddField(
            model_name='clasa',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='static/images/'),
        ),
    ]
