# Generated by Django 3.2.5 on 2022-02-16 17:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bmimodel',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='bmimodel',
            name='height',
        ),
        migrations.RemoveField(
            model_name='bmimodel',
            name='weight',
        ),
    ]