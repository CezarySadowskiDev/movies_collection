# Generated by Django 5.1.1 on 2024-10-20 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='duration',
            field=models.IntegerField(),
        ),
    ]