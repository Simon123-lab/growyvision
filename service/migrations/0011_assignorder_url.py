# Generated by Django 3.2.4 on 2021-09-01 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0010_alter_assignorder_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignorder',
            name='url',
            field=models.URLField(blank=True, max_length=500),
        ),
    ]
