# Generated by Django 3.2.9 on 2021-11-24 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quizappquestion',
            name='difficulty',
            field=models.CharField(choices=[('Easy', 'Easy'), ('Normal', 'Normal'), ('Hard', 'Hard')], max_length=100),
        ),
    ]
