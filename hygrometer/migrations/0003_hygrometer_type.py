# Generated by Django 3.0.6 on 2020-05-14 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hygrometer', '0002_auto_20200304_2220'),
    ]

    operations = [
        migrations.AddField(
            model_name='hygrometer',
            name='type',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
