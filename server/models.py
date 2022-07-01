from django.db import models


class Server(models.Model):
    name = models.CharField(max_length=20)
    ip_address = models.CharField(max_length=15)
    os_ver = models.CharField(max_length=10)
    port = models.CharField(max_length=4)

    def __str__(self):
        return self.name
    