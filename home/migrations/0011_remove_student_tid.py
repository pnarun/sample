# Generated by Django 2.2.2 on 2019-07-04 09:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_library_due_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='tid',
        ),
    ]
