# Generated by Django 3.2.5 on 2021-08-23 04:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BookDriveApp', '0009_delete_person'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='benif',
            new_name='benificiary',
        ),
    ]