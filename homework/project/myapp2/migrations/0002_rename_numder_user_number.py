# Generated by Django 5.0.6 on 2024-07-03 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp2', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='numder',
            new_name='number',
        ),
    ]
