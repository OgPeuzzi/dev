# Generated by Django 4.2.6 on 2023-10-16 16:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AidAuto', '0006_remove_demande_vehicule'),
    ]

    operations = [
        migrations.RenameField(
            model_name='demande',
            old_name='Admin_Demande',
            new_name='Full_name',
        ),
    ]
