# Generated by Django 3.0.8 on 2020-08-05 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp1', '0011_auto_20200805_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jalanpropinsi',
            name='fungsiJalanP',
            field=models.CharField(max_length=40, null=True),
        ),
    ]
