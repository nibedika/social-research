# Generated by Django 2.2.8 on 2020-01-16 18:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('elemental_fact', '0003_auto_20200116_2226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cl',
            name='correlation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='social_element_correlation', to='social_element.Cl'),
        ),
    ]
