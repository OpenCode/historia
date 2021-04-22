# Generated by Django 3.2 on 2021-04-21 23:26

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0005_document_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]
