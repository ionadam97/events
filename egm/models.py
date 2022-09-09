from django.db import models
from location.models import Location


class Egm(models.Model):

    serie = models.CharField(max_length=200)
    cabinet = models.ForeignKey(
        'Cabinet', null=True, blank=True, on_delete=models.DO_NOTHING)
    platforma = models.ForeignKey(
        'Platform', null=True, blank=True, on_delete=models.DO_NOTHING)
    locatia = models.ForeignKey(
        Location, null=True, blank=True, on_delete=models.DO_NOTHING)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.serie


class Cabinet(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.name


class Platform(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.name
