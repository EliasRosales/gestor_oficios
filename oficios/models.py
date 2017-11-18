# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Departments(models.Model):
    name = models.CharField(max_length=100)
    responsible = models.CharField(max_length=100)
    register_date = models.DateField(auto_now_add=True)
    delete_date = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=True)


class Sender(models.Model):
    department = models.CharField(max_length=100)
    responsible = models.CharField(max_length=100)
    register_date = models.DateField(auto_now_add=True)
    delete_date = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=True)


class Trades(models.Model):
    date_trades = models.DateField()
    description = models.TextField()
    folio = models.CharField(max_length=100)
    observations = models.TextField()
    departament = models.ForeignKey(Departments)
    sender = models.ForeignKey(Sender)
    register_date = models.DateField(auto_now_add=True)
    delete_date = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

