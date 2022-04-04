# Generated by Django 3.1.5 on 2022-03-12 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, null=True)),
                ('attachment', models.FileField(blank=True, max_length=50, null=True, upload_to='')),
                ('sharedlink', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
    ]