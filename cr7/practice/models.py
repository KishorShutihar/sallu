from django.db import models


class Actor(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(null=True, blank=True)
    description = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name

