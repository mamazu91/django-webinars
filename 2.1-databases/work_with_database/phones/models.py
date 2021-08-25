from django.db import models


class Phone(models.Model):
    name = models.TextField(null=False, blank=False)
    image = models.TextField(null=False, blank=False)
    price = models.IntegerField(null=False, blank=False)
    release_date = models.DateField(null=False, blank=False)
    lte_exists = models.BooleanField(null=False, blank=False)
    slug = models.TextField(null=False, blank=False)

    def __str(self):
        return f'{self.id}: {self.name}'
