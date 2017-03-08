from __future__ import unicode_literals

from django.db import models

# Create your models here.


from django.db import models
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible  # only if you need to support Python 2
class Question(models.Model):
    question_text = models.CharField(max_length=200,null=True)
    pub_date = models.DateTimeField('date published',null=True)
    def __str__(self):
        return self.question_text

@python_2_unicode_compatible  # only if you need to support Python 2
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE,null=True)
    choice_text = models.CharField(max_length=200,null=True)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text








