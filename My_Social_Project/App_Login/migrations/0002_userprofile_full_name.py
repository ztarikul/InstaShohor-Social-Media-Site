# Generated by Django 3.0.6 on 2020-07-14 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Login', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='full_name',
            field=models.CharField(blank=True, max_length=260),
        ),
    ]
