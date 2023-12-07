# Generated by Django 4.2.7 on 2023-12-04 04:08

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("contenttypes", "0002_remove_content_type_name"),
        ("genericRentalApp", "0002_alter_renteditem_content_type"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="renteditem",
            unique_together={("content_type", "object_id")},
        ),
    ]