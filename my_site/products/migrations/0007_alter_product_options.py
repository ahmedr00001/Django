# Generated by Django 5.1.5 on 2025-02-04 13:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_test_created'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['name'], 'verbose_name': 'product '},
        ),
    ]
