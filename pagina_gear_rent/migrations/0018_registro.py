# Generated by Django 4.2.1 on 2023-06-23 15:37

from django.db import migrations, models
import pagina_gear_rent.models


class Migration(migrations.Migration):

    dependencies = [
        ('pagina_gear_rent', '0017_delete_pack_product_oferta'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_completo', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('contraseña', models.CharField(max_length=100)),
                ('rut', models.CharField(max_length=12, validators=[pagina_gear_rent.models.validate_rut])),
            ],
        ),
    ]