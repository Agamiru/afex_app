# Generated by Django 4.0.6 on 2022-07-27 13:41

import afex_app.storage_backends
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0002_chat_respond_to_alter_chat_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='file',
            field=models.FileField(help_text='A file you wish to upload', null=True, upload_to=afex_app.storage_backends.MediaStorage()),
        ),
    ]
