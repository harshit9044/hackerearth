# Generated by Django 2.1.7 on 2019-02-18 15:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wine', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wine',
            name='id_number',
        ),
    ]