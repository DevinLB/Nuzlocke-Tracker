# Generated by Django 3.1.7 on 2021-04-12 07:29

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pkinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('pk_id', models.CharField(max_length=100)),
                ('jfield', django.contrib.postgres.fields.jsonb.JSONField()),
            ],
        ),
    ]