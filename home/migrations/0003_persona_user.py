# Generated by Django 3.1.7 on 2021-04-06 05:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0002_auto_20210406_0028'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='user',
            field=models.OneToOneField(default=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]