# Generated by Django 4.2.1 on 2023-06-17 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagina_gear_rent', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='img/'),
        ),
    ]