# Generated by Django 5.1 on 2024-08-13 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_app_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='app',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
    ]
