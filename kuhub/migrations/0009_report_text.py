# Generated by Django 3.1.1 on 2020-11-08 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kuhub', '0008_remove_report_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='text',
            field=models.TextField(default=50),
            preserve_default=False,
        ),
    ]
