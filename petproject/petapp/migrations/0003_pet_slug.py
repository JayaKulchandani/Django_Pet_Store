# Generated by Django 4.2.4 on 2023-12-27 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petapp', '0002_customer_alter_pet_managers'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]
