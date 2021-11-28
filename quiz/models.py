from django.db import models

class QuizAppCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Categories"

    @property
    def quiz_count(self):
        return self.quiz_set.count()

class QuizApp(models.Model):
    title = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(QuizAppCategory, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} | {self.category}'

    class Meta:
        verbose_name_plural = "Quizs"

    @property
    def question_count(self):
        return self.question_set.count()

class QuizUpdate(models.Model):
    updated = models.DateTimeField(auto_now=True)

    class Meta :
        abstract = True

class QuizAppQuestion(QuizUpdate):
    title = models.CharField(max_length=300, verbose_name="question")
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
        return f'{self.title}'

    class Meta:
        verbose_name_plural = "Questions"

class QuizAppAnswer(QuizUpdate):
    answer_text = models.CharField(max_length=300)
    is_right = models.BooleanField()
    question = models.ForeignKey(QuizAppQuestion, on_delete=models.CASCADE, related_name='answer')

    def __str__(self):
        return f'{self.answer_text} | {self.question}'

    class Meta:
        verbose_name_plural = "Answers"
    
