# Generated by Django 4.2.3 on 2023-08-07 05:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('perfumes', '0021_products_mrp12_products_sellingprice12'),
    ]

    operations = [
        migrations.CreateModel(
            name='productsize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(choices=[('50ML', '50ML'), ('6ML 12ML', '6ML 12ML'), ('6ML', '6ML'), ('12ML', '12ML')], max_length=20)),
                ('mrp', models.CharField(max_length=10)),
                ('sellingprice', models.CharField(max_length=10)),
                ('productid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='perfumes.products')),
            ],
        ),
    ]