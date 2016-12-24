

from django.db import models
from django.utils import timezone
from django.shortcuts import resolve_url as r
from datetime import timedelta


class Question(models.Model):
    question_text = models.CharField('texto', max_length=200)
    pub_date = models.DateTimeField('data de publicação')

    class Meta:
        verbose_name = 'Pergunta'
        verbose_name_plural = 'Perguntas'
        ordering = ['-pub_date']

    def published_recently(self):
        """Returns if it was published recently (range: 1 day)"""
        return self.pub_date >= timezone.now() - timedelta(days=1)

    def __str__(self):
        return self.question_text

    def get_absolute_url(self):
        return r('polls:detail', question_id=self.pk)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text






