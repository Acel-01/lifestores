# Generated by Django 4.0.2 on 2022-02-06 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0002_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='lifestores-assessment/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
        migrations.AlterField(
            model_name='product',
            name='sku',
            field=models.CharField(max_length=6),
        ),
    ]
