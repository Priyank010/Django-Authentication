# Generated by Django 4.0 on 2022-11-03 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=250),
        ),
    ]
