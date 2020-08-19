# Generated by Django 3.1 on 2020-08-10 14:15

from django.db import migrations, models

import saleor.core.utils.json_serializer


class Migration(migrations.Migration):

    dependencies = [
        ("checkout", "0026_auto_20200709_1102"),
    ]

    operations = [
        migrations.AlterField(
            model_name="checkout",
            name="metadata",
            field=models.JSONField(
                blank=True,
                default=dict,
                encoder=saleor.core.utils.json_serializer.CustomJsonEncoder,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="checkout",
            name="private_metadata",
            field=models.JSONField(
                blank=True,
                default=dict,
                encoder=saleor.core.utils.json_serializer.CustomJsonEncoder,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="checkoutline",
            name="data",
            field=models.JSONField(blank=True, default=dict),
        ),
    ]
