# Generated by Django 3.0.7 on 2020-06-23 13:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20200623_0941'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='date',
        ),
        migrations.AddField(
            model_name='blog',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='blog',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
