# Generated by Django 2.1.7 on 2019-04-21 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20190421_1328'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='url_test',
            field=models.URLField(default='www.pierre-dauphin.hoto.org'),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_temps',
            field=models.DateTimeField(),
        ),
    ]
