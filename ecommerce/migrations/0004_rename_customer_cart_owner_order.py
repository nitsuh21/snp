# Generated by Django 4.0.3 on 2022-05-23 06:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ecommerce', '0003_rename_owner_cart_customer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='Customer',
            new_name='owner',
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quantity', models.IntegerField(blank=True, default=1, null=True)),
                ('Subtotal', models.IntegerField(blank=True, default=0, null=True)),
                ('Total', models.IntegerField(blank=True, default=0, null=True)),
                ('Customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.product')),
            ],
        ),
    ]