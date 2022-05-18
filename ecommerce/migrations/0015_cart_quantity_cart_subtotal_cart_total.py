# Generated by Django 4.0.3 on 2022-05-17 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0014_cart_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='Quantity',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='cart',
            name='Subtotal',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='cart',
            name='Total',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]