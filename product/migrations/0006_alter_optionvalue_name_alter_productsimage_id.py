# Generated by Django 5.0.2 on 2024-03-02 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_rename_price_product_sell_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='optionvalue',
            name='name',
            field=models.CharField(max_length=255, null=True, verbose_name='Значение варианты'),
        ),
        migrations.AlterField(
            model_name='productsimage',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]