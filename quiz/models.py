from django.db import models
from django.db.models.fields.reverse_related import ManyToOneRel

class QuizAppCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class QuizApp(models.Model):
    title = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(QuizAppCategory, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} | {self.category}'

class QuizAppQuestion(models.Model):
    title = models.TextField()
    updated = models.DateTimeField(auto_now=True)

    DIFFICULT = {
        ('Easy', 'Easy'),
        ('Normal', 'Normal'),
        ('Hard', 'Hard')
    }
    difficulty = models.CharField(choices=DIFFICULT, max_length=100)

    date_created = models.DateTimeField(auto_now_add=True)
    quiz = models.ForeignKey(QuizApp, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} | {self.difficulty} | {self.quiz}'

class QuizAppAnswer(models.Model):
    updated = models.DateTimeField(auto_now=True)
    anwser_text = models.TextField()
    is_right = models.BooleanField()
    question = models.ForeignKey(QuizAppQuestion, on_delete=models.CASCADE)

    
