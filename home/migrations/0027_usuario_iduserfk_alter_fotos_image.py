# Generated by Django 4.0.3 on 2022-03-23 11:44

from django.db import migrations, models
import home.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0026_remove_fotos_nomeproduto'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='idUserFK',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='fotos',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=home.models.upload_image_produto),
        ),
    ]
