# Generated by Django 3.0.7 on 2020-06-09 08:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0007_auto_20200606_1419'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmark',
            name='last_accessed_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]