# Generated by Django 4.2.5 on 2023-09-14 15:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Todoapp',
            new_name='Tasks',
        ),
    ]
