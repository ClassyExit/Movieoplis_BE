# Generated by Django 5.1.4 on 2025-02-27 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_alter_user_firebase_uid'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='canViewVideos',
            field=models.BooleanField(default=False),
        ),
    ]
