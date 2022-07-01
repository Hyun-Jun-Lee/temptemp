from django.db import models
from server.models import Server


class Table(models.Model):
    server = models.ForeignKey(
        Server, on_delete=models.CASCADE, related_name="tables")
    name = models.CharField(max_length=20)
    db_platform = models.CharField(max_length=20)

    @property
    def systems_name(self):
        return [x.name for x in self.systems.all()]
