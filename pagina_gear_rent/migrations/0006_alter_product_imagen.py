# Generated by Django 4.2.1 on 2023-06-17 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagina_gear_rent', '0005_alter_product_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='img/'),
        ),
    ]
