from django.db import models
from server.models import Server


class Table(models.Model):
    server = models.ForeignKey(
        Server, on_delete=models.CASCADE, related_name="tables")
    name = models.CharField(max_length=20)
    db_platform = models.CharField(max_length=20)

    def __str__(self):
        return self.name