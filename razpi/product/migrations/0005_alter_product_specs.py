# Generated by Django 4.0.4 on 2022-06-21 23:15

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_product_specs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='specs',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]