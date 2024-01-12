# Generated by Django 4.2.4 on 2023-12-20 06:43

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('petapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=200)),
                ('phoneno', models.BigIntegerField()),
                ('password', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'customer',
            },
        ),
        migrations.AlterModelManagers(
            name='pet',
            managers=[
                ('pets', django.db.models.manager.Manager()),
            ],
        ),
    ]
