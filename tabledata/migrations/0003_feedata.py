# Generated by Django 4.1.3 on 2022-12-19 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tabledata', '0002_passoutdata'),
    ]

    operations = [
        migrations.CreateModel(
            name='feedata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('regno', models.CharField(max_length=50)),
                ('fee', models.CharField(max_length=50)),
                ('date', models.CharField(max_length=50)),
            ],
        ),
    ]
