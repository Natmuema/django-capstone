# Generated by Django 5.0.7 on 2024-08-03 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0006_alter_joblisting_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='joblisting',
            name='company',
            field=models.CharField(default='Unknown', max_length=255),
        ),
    ]
