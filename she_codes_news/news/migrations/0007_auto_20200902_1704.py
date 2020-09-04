# Generated by Django 3.0.8 on 2020-09-02 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_auto_20200901_1750'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newsstory',
            name='content',
        ),
        migrations.AddField(
            model_name='newsstory',
            name='extra_info',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='newsstory',
            name='ingredients',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='newsstory',
            name='method',
            field=models.TextField(default=''),
        ),
    ]
