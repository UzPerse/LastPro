# Generated by Django 5.0.2 on 2024-03-02 16:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_alter_productsimage_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='optionvalue',
            name='option',
        ),
        migrations.RemoveField(
            model_name='productvariant',
            name='option',
        ),
        migrations.RemoveField(
            model_name='productvariant',
            name='color',
        ),
        migrations.RemoveField(
            model_name='productvariant',
            name='product',
        ),
        migrations.DeleteModel(
            name='Option',
        ),
        migrations.DeleteModel(
            name='OptionValue',
        ),
        migrations.DeleteModel(
            name='ProductVariant',
        ),
    ]