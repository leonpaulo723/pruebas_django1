# Generated by Django 3.1.7 on 2021-06-17 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20210617_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='telefono',
            field=models.CharField(max_length=15),
        ),
    ]
