# Generated by Django 2.2.2 on 2019-07-02 09:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20190702_1433'),
    ]

    operations = [
        migrations.AddField(
            model_name='library',
            name='due_date',
            field=models.DateField(blank=True, default=django.utils.timezone.now, verbose_name='Due Date'),
            preserve_default=False,
        ),
    ]
