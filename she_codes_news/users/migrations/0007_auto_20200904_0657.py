# Generated by Django 3.0.8 on 2020-09-03 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20200903_2033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profile_picture',
            field=models.ImageField(blank=True, default='images/cake.jpeg', null=True, upload_to='images/'),
        ),
    ]