# Generated by Django 3.0.8 on 2020-08-27 13:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0015_auto_20200827_0034'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='category',
            new_name='name',
        ),
    ]
