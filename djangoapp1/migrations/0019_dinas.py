# Generated by Django 2.2 on 2021-03-23 05:06

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp1', '0018_auto_20200812_1156'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dinas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dinas', models.CharField(max_length=70)),
                ('posisi', models.CharField(max_length=30)),
                ('ASN', models.IntegerField()),
                ('nonASN', models.IntegerField()),
                ('sd', models.IntegerField()),
                ('smp', models.IntegerField()),
                ('sma', models.IntegerField()),
                ('d1', models.IntegerField()),
                ('d2', models.IntegerField()),
                ('d3', models.IntegerField()),
                ('d4', models.IntegerField()),
                ('s1', models.IntegerField()),
                ('s2', models.IntegerField()),
                ('s3', models.IntegerField()),
                ('gol1a', models.IntegerField()),
                ('gol1b', models.IntegerField()),
                ('gol1c', models.IntegerField()),
                ('gol1d', models.IntegerField()),
                ('gol2a', models.IntegerField()),
                ('gol2b', models.IntegerField()),
                ('gol2c', models.IntegerField()),
                ('gol2d', models.IntegerField()),
                ('gol3a', models.IntegerField()),
                ('gol3b', models.IntegerField()),
                ('gol3c', models.IntegerField()),
                ('gol3d', models.IntegerField()),
                ('gol4a', models.IntegerField()),
                ('gol4b', models.IntegerField()),
                ('gol4c', models.IntegerField()),
                ('gol4d', models.IntegerField()),
                ('gol4e', models.IntegerField()),
                ('keterangan', models.TextField(max_length=100, null=True)),
                ('geometry', django.contrib.gis.db.models.fields.MultiLineStringField(null=True, srid=4326)),
            ],
            options={
                'verbose_name_plural': '8. Dinas Kabupaten OKUS',
            },
        ),
    ]
