# Generated by Django 3.0.6 on 2020-05-28 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='inventory',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('sku_code', models.CharField(max_length=60)),
                ('price', models.IntegerField()),
                ('stock', models.IntegerField()),
                ('created_by', models.CharField(max_length=60)),
                ('created_at', models.DateTimeField(verbose_name='created at')),
                ('updated_at', models.DateTimeField(verbose_name='updated at')),
            ],
        ),
    ]
