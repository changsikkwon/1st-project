# Generated by Django 3.0.8 on 2020-08-21 22:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User_information',
            new_name='UserInformation',
        ),
    ]