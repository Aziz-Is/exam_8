# Generated by Django 4.1 on 2022-08-27 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='images/koaf.jpg', upload_to='images/'),
        ),
    ]