# Generated by Django 3.1.7 on 2021-06-19 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_auto_20210619_0124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='marca',
            field=models.CharField(max_length=20),
        ),
    ]
