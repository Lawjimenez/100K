# Generated by Django 3.2.5 on 2021-08-24 04:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BookDriveApp', '0010_rename_benif_benificiary'),
    ]

    operations = [
        migrations.RenameField(
            model_name='benificiary',
            old_name='numberofbooks',
            new_name='countofbooks',
        ),
    ]
