# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class CreatreUser(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True, null=False)
    login_users = models.CharField(max_length=30, blank=True, null=True)
    paass_users = models.CharField(max_length=130, blank=True, null=True)

    class Meta:
        #managed = True
        ordering = ('id',)
        db_table = 'createuser'