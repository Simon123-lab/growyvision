# Generated by Django 3.2.4 on 2021-09-01 16:52

from django.db import migrations
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0009_auto_20210826_1014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignorder',
            name='video',
            field=embed_video.fields.EmbedVideoField(blank=True),
        ),
    ]
