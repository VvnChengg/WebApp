# Generated by Django 4.1 on 2023-05-07 12:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('item_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('transaction_type', models.CharField(max_length=20)),
                ('transaction_location', models.CharField(blank=True, max_length=100)),
                ('quantity', models.IntegerField()),
                ('category', models.CharField(max_length=20)),
                ('condition', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.item')),
            ],
        ),
    ]
