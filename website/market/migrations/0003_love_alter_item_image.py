# Generated by Django 4.2.1 on 2023-06-05 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0002_alter_item_transaction_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Love',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=100)),
                ('item', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]