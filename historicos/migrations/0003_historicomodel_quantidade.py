# Generated by Django 3.2.8 on 2021-11-11 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('historicos', '0002_historicomodel_observacao'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicomodel',
            name='quantidade',
            field=models.PositiveSmallIntegerField(default=None),
        ),
    ]