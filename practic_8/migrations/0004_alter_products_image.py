# Generated by Django 5.0.6 on 2024-07-10 06:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('practic_8', '0003_alter_products_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='practic_8.image'),
        ),
    ]
