# Generated by Django 3.1.2 on 2020-10-25 08:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tugas2', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mengemas',
            name='tgl_kemas',
            field=models.DateField(default=datetime.date.today),
        ),
    ]