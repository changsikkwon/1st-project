# Generated by Django 3.0.8 on 2020-08-23 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_auto_20200822_2020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image_url',
            field=models.URLField(max_length=2048, null=True),
        ),
    ]
