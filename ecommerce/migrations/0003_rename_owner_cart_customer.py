# Generated by Django 4.0.3 on 2022-05-23 06:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0002_product_quantity'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='owner',
            new_name='Customer',
        ),
    ]