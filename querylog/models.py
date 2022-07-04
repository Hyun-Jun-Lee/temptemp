from django.db import models
from table.models import Table


class Querylog(models.Model):
    table = models.ForeignKey(
        Table, on_delete=models.SET_NULL, related_name="querylogs", blank=True, null=True)
    sr_number = models.CharField(max_length=20, blank=True, null=True)
    query_info = models.TextField()

    query_type_choices = (
        ('SELECT','SELECT'),
        ('INSERT', 'INSERT'),
        ('UPDATE','UPDATE'),
        ('DELETE','DELETE'),
        ('CREATE','CREATE'),
        ('ALTER','ALTER'),
        ('TRUNCATE','TRUNCATE'),
        ('DROP','DROP'),
        ('DESCRIBE','DESCRIBE'),
        ('RENAME','RENAME')
    )

    query_type = models.CharField(max_length=10, choices=query_type_choices)
    request_time = models.DateTimeField(auto_now_add=True)
    manager = models.CharField(max_length=20, blank=True, null=True)

    @property
    def server_name(self):
        return self.table.server.name

    @property
    def system_name(self):
        return [i for i in self.table.system_names]