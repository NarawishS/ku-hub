# Generated by Django 3.1.1 on 2020-11-08 16:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('kuhub', '0014_auto_20201108_2316'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Report',
            new_name='BlogReport',
        ),
        migrations.CreateModel(
            name='CommentReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(choices=[('Fake new', 'Fake new'), ('Spam', 'Spam'), ('Create conflict', 'Create conflict'), ('Threat', 'Threat'), ('Violence', 'Violence'), ('Indecent words', 'Indecent words'), ('Others', 'Others')], max_length=20)),
                ('text', models.TextField(blank=True, default='')),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reports', to='kuhub.comment')),
            ],
        ),
    ]
