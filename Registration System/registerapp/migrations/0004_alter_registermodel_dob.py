# Generated by Django 4.0.6 on 2022-07-30 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registerapp', '0003_alter_registermodel_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registermodel',
            name='dob',
            field=models.DateField(default='2002-05-27'),
        ),
    ]