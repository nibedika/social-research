# Generated by Django 2.2.8 on 2020-01-13 15:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('access', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='designation',
            field=models.SlugField(default='admin', validators=[django.core.validators.RegexValidator]),
        ),
    ]