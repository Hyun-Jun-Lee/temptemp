from django.db import models
from table.models import Table


class Querylog(models.Model):
    table = models.ForeignKey(
        Table, on_delete=models.CASCADE, related_name="querylogs")
    sr_number = models.CharField(max_length=20, blank=True, null=True)
    query_info = models.TextField()
    query_type = models.CharField(max_length=10)
    requerst_time = models.DateTimeField(auto_now_add=True)
    manager = models.CharField(max_length=20)

    @property
    def server_name(self):
        return self.table.server.name

    @property
    def systems_name(self):
        return self.table.systems_name