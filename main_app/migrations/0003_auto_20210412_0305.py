# Generated by Django 3.1.7 on 2021-04-12 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_pkinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pkinfo',
            name='jfield',
            field=models.JSONField(),
        ),
    ]