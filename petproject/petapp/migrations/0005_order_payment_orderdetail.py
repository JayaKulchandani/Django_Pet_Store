# Generated by Django 4.2.4 on 2024-01-09 06:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('petapp', '0004_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=500)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('pincode', models.CharField(max_length=100)),
                ('ordernumber', models.CharField(max_length=100)),
                ('phoneno', models.BigIntegerField()),
            ],
            options={
                'db_table': 'order',
            },
        ),
        migrations.CreateModel(
            name='payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paymentstatus', models.CharField(default='pending', max_length=100)),
                ('transactionid', models.CharField(max_length=200)),
                ('paymentmode', models.CharField(default='paypal', max_length=100)),
                ('customerid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='petapp.customer')),
                ('oid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='petapp.order')),
            ],
            options={
                'db_table': 'payment',
            },
        ),
        migrations.CreateModel(
            name='orderdetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordernumber', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
                ('totalprice', models.IntegerField()),
                ('created_at', models.DateField(auto_now=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('customerid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='petapp.customer')),
                ('paymentid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='petapp.payment')),
                ('productid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='petapp.pet')),
            ],
            options={
                'db_table': 'orderdetail',
            },
        ),
    ]
