# Generated by Django 3.0.6 on 2020-05-26 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0007_auto_20200526_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image_pics',
            field=models.ImageField(upload_to='images/'),
        ),
    ]