from django.db import models

from django.contrib.auth.models import User


class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Question(models.Model):
    question = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question

    # def __str__(self):
    #     return f"{self.title}-{self.group}"


class Choice(models.Model):
    question = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=100)

    def __str__(self):
        return self.choice_text


class UserSelection(models.Model):
    choice = models.ForeignKey(Choice, related_name='selections', on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_by = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("question", "selected_by")
