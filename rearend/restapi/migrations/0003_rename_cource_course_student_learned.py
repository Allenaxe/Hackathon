# Generated by Django 5.0.1 on 2024-01-26 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0002_student'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cource',
            new_name='Course',
        ),
        migrations.AddField(
            model_name='student',
            name='Learned',
            field=models.TextField(default=''),
        ),
    ]