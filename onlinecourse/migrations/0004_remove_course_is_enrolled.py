# Generated by Django 5.0.1 on 2024-01-12 18:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0003_alter_course_id_alter_enrollment_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='is_enrolled',
        ),
    ]
