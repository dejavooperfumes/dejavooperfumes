# Generated by Django 4.2.3 on 2023-08-01 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfumes', '0017_products_photo3'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='mrp12',
            field=models.CharField(default='Oriental', max_length=10),
        ),
        migrations.AddField(
            model_name='products',
            name='sellingprice12',
            field=models.CharField(default='Oriental', max_length=10),
        ),
    ]
