# Generated by Django 4.0.4 on 2022-08-22 20:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_orderitem_quantity'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ('-created_at',)},
        ),
        migrations.RenameField(
            model_name='order',
            old_name='pain_amount',
            new_name='paid_amount',
        ),
    ]
