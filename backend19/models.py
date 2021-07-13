# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
from django.urls import reverse


class CreateDb(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True, null=False)
    tovarname = models.CharField(max_length=30, blank=True, null=True)
    price = models.CharField(max_length=30, blank=True, null=True)
    sale = models.CharField(max_length=30, blank=True, null=True)
    category = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        #managed = True
        ordering = ('id',)
        db_table = 'test_DB19'

    def get_absolute_url(self):
        return reverse("backendoutpk19",  args=[str(self.id)])
        # return reverse("backendoutpk19", kwargs={"id" : self.id})