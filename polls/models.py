# This file contains the models for the polls app
import datetime

from django.db import models
from django.utils import timezone
# Question model will be where questions and their attributes will be stored.
# Each field below the model is esentially a column in the database
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __unicode__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
# The Choice model will be where the possible answers to the Questions will be stored
# Each field below the model is esentially a column in the database
# The question field relates each choice to one single question

class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __unicode__(self):
        return self.choice_text
