# Generated by Django 4.2.1 on 2023-06-23 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagina_gear_rent', '0016_pack'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Pack',
        ),
        migrations.AddField(
            model_name='product',
            name='oferta',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
