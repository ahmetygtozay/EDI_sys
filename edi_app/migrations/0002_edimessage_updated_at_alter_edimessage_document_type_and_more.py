# Generated by Django 5.1.2 on 2024-10-31 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edi_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='edimessage',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='edimessage',
            name='document_type',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='edimessage',
            name='receiver',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='edimessage',
            name='sender',
            field=models.CharField(max_length=255),
        ),
    ]