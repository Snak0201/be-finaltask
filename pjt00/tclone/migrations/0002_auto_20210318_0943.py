# Generated by Django 3.1.7 on 2021-03-18 00:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tclone', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tweet',
            name='tweet',
            field=models.CharField(max_length=140),
        ),
    ]
