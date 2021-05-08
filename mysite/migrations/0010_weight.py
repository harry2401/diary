# Generated by Django 3.1.7 on 2021-05-04 21:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0009_auto_20210206_1726'),
    ]

    operations = [
        migrations.CreateModel(
            name='Weight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reading_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('weight', models.DecimalField(blank=True, decimal_places=1, max_digits=4, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('glucose', models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True)),
                ('HbA1c', models.DecimalField(blank=True, decimal_places=0, max_digits=2, null=True)),
                ('blood_pressure_1', models.DecimalField(blank=True, decimal_places=0, max_digits=3, null=True)),
                ('blood_pressure_2', models.DecimalField(blank=True, decimal_places=0, max_digits=3, null=True)),
                ('HDL', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('LDL', models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True)),
                ('created_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
            ],
        ),
    ]