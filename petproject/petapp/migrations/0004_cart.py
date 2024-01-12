# Generated by Django 4.2.4 on 2024-01-02 06:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('petapp', '0003_pet_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('totalamount', models.FloatField()),
                ('customerid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='petapp.customer')),
                ('productid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='petapp.pet')),
            ],
            options={
                'db_table': 'cart',
            },
        ),
    ]
