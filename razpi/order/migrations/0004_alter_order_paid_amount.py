# Generated by Django 4.0.4 on 2022-08-23 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_alter_order_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='paid_amount',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
