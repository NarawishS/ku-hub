# Generated by Django 3.1.1 on 2020-11-08 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kuhub', '0011_auto_20201108_2240'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='topic',
            field=models.CharField(choices=[('Fake new', 'Fake new'), ('Spam', 'Spam'), ('Create conflict', 'Create conflict'), ('Threat', 'Threat'), ('Violence', 'Violence'), ('Indecent words', 'Indecent words'), ('Others', 'Others')], default=1, max_length=20),
            preserve_default=False,
        ),
    ]