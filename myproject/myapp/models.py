from django.db import models

class Article (models.Model):
title = models.CharField (max_lenght=200)
content = models.TextField ()
pub_date = models.DateTimeField (auto_now_add=True)