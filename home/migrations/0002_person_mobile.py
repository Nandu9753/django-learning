# Generated by Django 4.2.1 on 2023-09-28 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='mobile',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
