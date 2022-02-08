# Generated by Django 4.0.2 on 2022-02-06 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('age', models.PositiveIntegerField(default=0)),
                ('sex', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=200)),
            ],
        ),
    ]
