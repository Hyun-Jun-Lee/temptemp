from django.db import models


class System(models.Model):
    name = models.CharField(max_length=20)
    system_description = models.TextField()
