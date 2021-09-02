from django.db import models

# Create your models here.
class Exam(models.Model):
    id = models.AutoField(primary_key=True)
    Question = models.CharField(max_length=100, default="null")
    opt1 = models.CharField(max_length=100, default="null")
    opt2 = models.CharField(max_length=100, default="null")
    opt3 = models.CharField(max_length=100, default="null")
    opt4 = models.CharField(max_length=100, default="null")
    correct_ans = models.CharField(max_length=100, default="null")

    def __str__(self):
        return str(self.id)