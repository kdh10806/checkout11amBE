# Generated by Django 4.0.3 on 2022-04-13 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('residences', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='residence',
            name='address',
            field=models.CharField(default='', max_length=200),
        ),
    ]
