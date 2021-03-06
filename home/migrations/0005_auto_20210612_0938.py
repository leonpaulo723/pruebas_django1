# Generated by Django 3.1.7 on 2021-06-12 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20210406_0106'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicio',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='servicios'),
        ),
        migrations.AddField(
            model_name='servicio',
            name='tiempo',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='servicio',
            name='descripcion',
            field=models.TextField(max_length=5000),
        ),
    ]
