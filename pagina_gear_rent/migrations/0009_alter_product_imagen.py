# Generated by Django 4.2.1 on 2023-06-18 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagina_gear_rent', '0008_alter_product_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]