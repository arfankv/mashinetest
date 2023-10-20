# Generated by Django 4.2.6 on 2023-10-20 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=254)),
                ('Number', models.CharField(max_length=10)),
                ('age', models.CharField(max_length=10)),
                ('course', models.CharField(choices=[('python', 'python'), ('flutter', 'Flutter'), ('php', 'php'), ('Mernstack', 'MERNSTACK'), ('.net', '.Net')], default='python', max_length=10)),
            ],
        ),
    ]