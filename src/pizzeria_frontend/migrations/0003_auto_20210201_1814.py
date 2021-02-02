# Generated by Django 3.1.5 on 2021-02-01 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzeria_frontend', '0002_auto_20210201_1230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]