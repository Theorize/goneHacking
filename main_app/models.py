'''pylinter bugger off'''
from __future__ import unicode_literals
from django.utils import timezone
from django.db import models

# Create your models here.
class Status(models.Model):
    '''Status thing'''
    time = models.DateTimeField(editable=False)
    text = models.CharField(max_length=500)

    def save(self, *args, **kwargs):
        ''' On save, update timestamp '''
        if not self.id:
            self.time = timezone.now()
        return super(Status, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.time)
# trust_levels = none, close relatives, relatives and network

class Category(models.Model):
    ''' Category Trust Levels.'''
    category = models.CharField(max_length=50)
    trust_level = models.CharField(max_length=20)
    priority = models.IntegerField()

    def __str__(self):
        return str(self.category) + " " + str(self.trust_level)


class Task(models.Model):
    '''Task thing'''
    creation_date = models.DateTimeField(editable=False)
    category = models.ForeignKey(Category)
    task = models.CharField(max_length=100)
    notes = models.CharField(max_length=200, blank=True)
    day_one = models.CharField(max_length=3, blank=True, default=None)
    day_two = models.CharField(max_length=3, blank=True, default=None)
    day_three = models.CharField(max_length=3, blank=True, default=None)
    day_four = models.CharField(max_length=3, blank=True, default=None)
    day_five = models.CharField(max_length=3, blank=True, default=None)
    day_six = models.CharField(max_length=3, blank=True, default=None)
    day_seven = models.CharField(max_length=3, blank=True, default=None)

    def save(self, *args, **kwargs):
        ''' On save, update timestamp '''
        if not self.id:
            self.creation_date = timezone.now()
        return super(Task, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.task)
