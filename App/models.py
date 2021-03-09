# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User



class Post(models.Model):
    autor = models.ForeignKey(User)
    texto = models.TextField()

    actualizar = models.DateTimeField(auto_now=True)
    creado = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['creado']

    def __unicode__(self):
        return self.text+' - '+self.author.username