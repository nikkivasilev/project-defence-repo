# Generated by Django 4.1.3 on 2022-12-11 15:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_remove_product_quantity'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('-price',)},
        ),
    ]
