# Generated by Django 5.1.4 on 2025-02-19 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_alter_listitem_item_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listitem',
            name='item_id',
            field=models.IntegerField(default=0),
        ),
    ]
