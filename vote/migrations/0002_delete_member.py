# Generated by Django 3.2.8 on 2021-10-25 18:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Member',
        ),
    ]