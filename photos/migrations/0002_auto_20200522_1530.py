# Generated by Django 3.0.6 on 2020-05-22 12:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='imange_name',
            new_name='image_name',
        ),
    ]