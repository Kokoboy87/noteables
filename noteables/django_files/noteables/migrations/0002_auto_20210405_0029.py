# Generated by Django 2.2 on 2021-04-05 04:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('noteables', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='note_content',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='note',
            old_name='note_title',
            new_name='title',
        ),
    ]
