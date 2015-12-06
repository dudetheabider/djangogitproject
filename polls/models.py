# This file contains the models for the polls app

from django.db import models

# Question model will be where questions and their attributes will be stored.
# Each field below the model is esentially a column in the database
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

# The Choice model will be where the possible answers to the Questions will be stored
# Each field below the model is esentially a column in the database
# The question field relates each choice to one single question

class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

