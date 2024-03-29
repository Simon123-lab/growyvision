# Generated by Django 3.2.4 on 2021-08-20 20:26

from django.db import migrations, models
import django.db.models.deletion
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0006_alter_order_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssignOrder',
            fields=[
                ('assign_id', models.AutoField(primary_key=True, serialize=False)),
                ('assign_at', models.DateTimeField(auto_now_add=True)),
                ('reciept', models.CharField(choices=[('VID101', 'VID101'), ('LIK101', 'LIK101'), ('FOL101', 'FOL101')], max_length=30)),
                ('video', embed_video.fields.EmbedVideoField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.order')),
            ],
        ),
    ]
