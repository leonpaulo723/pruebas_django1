# Generated by Django 3.1.7 on 2021-06-19 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_auto_20210619_0141'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cita',
            name='jornada',
        ),
        migrations.AlterField(
            model_name='cita',
            name='hora',
            field=models.CharField(choices=[('8:00 - 9:00', '8:00 - 9:00'), ('9:00 - 10:00', '9:00 - 10:00'), ('10:00 - 11:00', '10:00 - 11:00'), ('11:00 - 12:00', '11:00 - 12:00')], max_length=15),
        ),
    ]
