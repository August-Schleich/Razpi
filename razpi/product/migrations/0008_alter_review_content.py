# Generated by Django 4.0.4 on 2022-08-23 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_alter_category_options_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='content',
            field=models.TextField(),
        ),
    ]
