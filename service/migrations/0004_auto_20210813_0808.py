# Generated by Django 3.2.4 on 2021-08-13 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0003_rename_quantity_order_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='phone_no',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('In Process', 'In Process'), ('Cancelled', 'Cancelled'), ('Completed', 'Completed')], default='pending', max_length=50),
        ),
    ]