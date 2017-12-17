# Generated by Django 2.0 on 2017-12-17 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database_practice', '0003_auto_20171217_2153'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fruit',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Fruit2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
    ]
