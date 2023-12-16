# Generated by Django 4.1.3 on 2022-12-07 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tabledata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg', models.CharField(max_length=15)),
                ('name', models.CharField(max_length=40)),
                ('fathername', models.CharField(max_length=10)),
                ('mothername', models.CharField(max_length=20)),
                ('phoneno', models.CharField(max_length=40)),
                ('address', models.CharField(max_length=40)),
                ('city', models.CharField(max_length=40)),
                ('gender', models.CharField(max_length=40)),
                ('course', models.CharField(max_length=40)),
                ('btime', models.CharField(max_length=40)),
                ('photo', models.CharField(max_length=40)),
                ('fee', models.CharField(max_length=40)),
                ('refee', models.CharField(max_length=20)),
            ],
        ),
    ]
