# Generated by Django 5.0.3 on 2024-03-17 08:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_staff_staff_photo_alter_staff_department_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='Staff_Photo',
        ),
    ]
