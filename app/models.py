from django.db import models
from django import forms
from django.utils import timezone

class WeatherList(models.Model):
    today = models.DateTimeField(default=timezone.now)
    Low1 = 1
    Low2 = 2
    Low3 = 3
    Normal4 = 4
    Normal5 = 5
    Normal6 = 6
    High7 = 7
    High8 = 8
    High9 = 9
    High10 = 10
    CHOICES = (
    (Low1, '1'),
    (Low2, '2'),
    (Low3, '3'),
    (Normal4,'4'),
    (Normal5,'5'),
    (Normal6,'6'),
    (High7, '7'),
    (High8, '8'),
    (High9, '9'),
    (High10, '10'),
  )

    mood = models.IntegerField(choices=CHOICES, default= '1')

    note = models.CharField(max_length=100)

    training = models.BooleanField(default=True)

    def __str__(self):
        return self.note


