# Generated by Django 5.0.2 on 2024-03-02 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_alter_optionvalue_name_alter_productsimage_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productsimage',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
