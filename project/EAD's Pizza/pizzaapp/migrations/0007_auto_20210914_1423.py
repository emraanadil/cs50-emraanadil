# Generated by Django 3.1.7 on 2021-09-14 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzaapp', '0006_ordermodel_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermodel',
            name='status',
            field=models.CharField(default='Pending', max_length=10),
        ),
    ]
