# Generated by Django 5.1.6 on 2025-03-04 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0004_question_type_choices'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choices',
            old_name='quiz',
            new_name='question',
        ),
        migrations.AlterField(
            model_name='question',
            name='answer',
            field=models.CharField(max_length=255),
        ),
    ]
