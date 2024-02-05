# Generated by Django 4.2.6 on 2023-10-17 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AidAuto', '0007_rename_admin_demande_demande_full_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='register',
            old_name='nom_d_utilisateur',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='register',
            old_name='password_hash',
            new_name='last_name',
        ),
        migrations.AddField(
            model_name='register',
            name='password',
            field=models.CharField(default='', max_length=350),
        ),
    ]