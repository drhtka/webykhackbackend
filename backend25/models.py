# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class CreateDb(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True, null=False)
    tovarname = models.CharField(max_length=30, blank=True, null=True)
    price = models.CharField(max_length=30, blank=True, null=True)
    sale = models.CharField(max_length=30, blank=True, null=True)
    category = models.CharField(max_length=30, blank=True, null=True)
    comment_one = models.CharField('Коммент 1', max_length=30, blank=True, null=True)
    comment_two = models.CharField('Коммент 2', max_length=30, blank=True, null=True)

    class Meta:
        #managed = True
        ordering = ('id',)
        db_table = 'test_DB25'