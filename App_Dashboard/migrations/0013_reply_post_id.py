# Generated by Django 2.1.11 on 2022-01-03 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Dashboard', '0012_reply'),
    ]

    operations = [
        migrations.AddField(
            model_name='reply',
            name='post_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]