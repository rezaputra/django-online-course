# Generated by Django 5.0.1 on 2024-01-12 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='is_enrolled',
            field=models.BooleanField(default=False),
        ),
    ]
