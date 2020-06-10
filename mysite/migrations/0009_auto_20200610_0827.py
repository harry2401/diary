# Generated by Django 3.0.7 on 2020-06-10 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0008_bookmark_last_accessed_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmark',
            name='priority',
            field=models.IntegerField(default=100),
        ),
        migrations.AddField(
            model_name='category',
            name='priority',
            field=models.IntegerField(default=100),
        ),
        migrations.AddField(
            model_name='emailhost',
            name='priority',
            field=models.IntegerField(default=100),
        ),
        migrations.AddField(
            model_name='identifier',
            name='priority',
            field=models.IntegerField(default=100),
        ),
        migrations.AddField(
            model_name='identifier2',
            name='priority',
            field=models.IntegerField(default=100),
        ),
        migrations.AddField(
            model_name='login',
            name='priority',
            field=models.IntegerField(default=100),
        ),
    ]
