# Generated by Django 2.1.11 on 2021-12-03 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Login', '0004_userprofile_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='type',
            field=models.IntegerField(blank=True, max_length=264),
        ),
    ]
