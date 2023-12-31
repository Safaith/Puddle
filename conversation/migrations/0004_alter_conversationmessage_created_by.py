# Generated by Django 4.1.7 on 2023-08-24 15:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('conversation', '0003_conversationmessage_created_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conversationmessage',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_messages', to=settings.AUTH_USER_MODEL),
        ),
    ]
