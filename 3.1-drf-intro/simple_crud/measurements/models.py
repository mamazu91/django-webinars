from django.db import models


class TimestampFields(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        abstract = True


class Project(TimestampFields):
    name = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    image = models.ImageField(
        null=True,
        blank=True
    )


class Measurement(TimestampFields):
    value = models.FloatField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
