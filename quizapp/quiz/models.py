from django.db import models

# Create your models here.

class Question(models.Model):

    def __str__(self):
        return self.question
    
    question = models.CharField(max_length=1000)
    answer_a = models.CharField(max_length=1000)
    answer_b = models.CharField(max_length=1000)
    answer_c = models.CharField(max_length=1000)
    answer_d = models.CharField(max_length=1000)
    selected_answer = models.CharField(max_length=1000)
    correct_answer = models.CharField(max_length=1000)
