# Generated by Django 4.2 on 2024-11-14 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Shop", "0015_product_condition_product_eco_friendly_certification_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="image",
            field=models.ImageField(default="default.png", upload_to="products/"),
        ),
    ]
