# Generated by Django 3.2.7 on 2021-09-16 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Dashboard', '0002_alter_country_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='status',
            field=models.IntegerField(choices=[(1, 'Active'), (2, 'Deactivate')]),
        ),
    ]
