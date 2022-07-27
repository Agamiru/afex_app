# Generated by Django 4.0.6 on 2022-07-27 10:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='respond_to',
            field=models.ForeignKey(help_text='Chat ID you want to respond to', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='responses', to='chats.chat'),
        ),
        migrations.AlterField(
            model_name='chat',
            name='message',
            field=models.TextField(help_text='Chat message', max_length=500, null=True),
        ),
    ]
