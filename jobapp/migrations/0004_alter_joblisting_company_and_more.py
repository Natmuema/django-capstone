# Generated by Django 5.0.7 on 2024-08-03 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0003_alter_joblisting_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='joblisting',
            name='company',
            field=models.CharField(default='Unknown', max_length=255),
        ),
        migrations.AlterField(
            model_name='joblisting',
            name='job_industry',
            field=models.CharField(default='Unknown', max_length=255),
        ),
    ]
