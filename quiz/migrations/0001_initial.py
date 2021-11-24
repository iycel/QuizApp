# Generated by Django 3.2.9 on 2021-11-24 17:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QuizApp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='QuizAppCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='QuizAppQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('updated', models.DateTimeField(auto_now=True)),
                ('difficulty', models.CharField(max_length=100)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.quizapp')),
            ],
        ),
        migrations.CreateModel(
            name='QuizAppAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('anwser_text', models.TextField()),
                ('is_right', models.BooleanField()),
                ('question', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='quiz.quizappquestion')),
            ],
        ),
        migrations.AddField(
            model_name='quizapp',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.quizappcategory'),
        ),
    ]