# Generated by Django 3.0.5 on 2020-04-27 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pollmodel',
            name='count1',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='pollmodel',
            name='count2',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='pollmodel',
            name='count3',
            field=models.IntegerField(default=0),
        ),
    ]