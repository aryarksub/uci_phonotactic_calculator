# Generated by Django 2.1.7 on 2022-04-25 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webcalc', '0002_defaultfile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='defaultfile',
            name='training_file',
            field=models.FileField(upload_to='default'),
        ),
    ]