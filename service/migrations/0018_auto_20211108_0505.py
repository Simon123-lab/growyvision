# Generated by Django 3.2.4 on 2021-11-08 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0017_rename_category_package_form_p_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='Is_client',
            field=models.BooleanField(blank=True, default=False, verbose_name='Is client'),
        ),
        migrations.AlterField(
            model_name='user',
            name='Is_worker',
            field=models.BooleanField(blank=True, default=False, verbose_name='Is worker'),
        ),
    ]