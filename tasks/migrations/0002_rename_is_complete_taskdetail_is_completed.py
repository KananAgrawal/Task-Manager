# Generated by Django 4.1.2 on 2023-07-29 12:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='taskdetail',
            old_name='is_complete',
            new_name='is_completed',
        ),
    ]