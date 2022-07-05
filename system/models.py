from django.db import models
from table.models import Table


class System(models.Model):
    name = models.CharField(max_length=20, unique=True)
    description = models.TextField()
    tables = models.ManyToManyField(Table, related_name="systems")

    def __str__(self):
        return self.name

    def table_names(self):
        return [x.name for x in self.tables]



