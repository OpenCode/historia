# Generated by Django 3.2 on 2021-04-21 23:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0007_document_typology'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='donor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='album.donor'),
        ),
    ]