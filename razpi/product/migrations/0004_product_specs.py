# Generated by Django 4.0.4 on 2022-06-21 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_product_image_product_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='specs',
            field=models.TextField(blank=True, null=True),
        ),
    ]
