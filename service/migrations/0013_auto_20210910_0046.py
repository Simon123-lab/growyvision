# Generated by Django 3.2.4 on 2021-09-10 07:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0012_frequentlyaskquestions_robotconfirmationviews_updateweeklycontest'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='robotconfirmationviews',
            name='hero_task',
        ),
        migrations.CreateModel(
            name='WithdrawAmount',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('payment_method', models.CharField(choices=[('JazzCash', 'JazzCash'), ('EasyPaisa', 'EasyPaisa')], default='JazzCash', max_length=100)),
                ('acc_number', models.CharField(help_text='Account number of selected payment method', max_length=100)),
                ('req_status', models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Confirmed', 'Confirmed')], default='Pending', max_length=100)),
                ('requested_at', models.DateTimeField(auto_now_add=True)),
                ('confirmed_at', models.DateTimeField(auto_now=True)),
                ('user_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
