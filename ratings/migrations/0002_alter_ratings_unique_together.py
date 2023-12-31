# Generated by Django 4.1.6 on 2023-08-02 17:36

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0002_alter_product_barcode"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("ratings", "0001_initial"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="ratings",
            unique_together={("product", "user")},
        ),
    ]
