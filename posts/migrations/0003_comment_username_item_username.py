# Generated by Django 4.1 on 2023-05-14 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20230508_0203'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='username',
            field=models.CharField(default='visitor', max_length=100),
        ),
        migrations.AddField(
            model_name='item',
            name='username',
            field=models.CharField(default='visitor', max_length=100),
        ),
    ]