# Generated by Django 4.2.6 on 2023-10-20 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_cource'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cource',
            name='course',
            field=models.CharField(max_length=100),
        ),
    ]
