# Generated by Django 4.2.4 on 2024-01-10 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petapp', '0005_order_payment_orderdetail'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='totalbillamount',
            field=models.FloatField(default=0),
        ),
    ]