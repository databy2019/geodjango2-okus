# Generated by Django 3.0.8 on 2020-08-02 03:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp1', '0006_auto_20200802_0938'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='kecamatan',
            options={'ordering': ('kodeKec',), 'verbose_name_plural': 'Daftar Kecamatan'},
        ),
    ]
