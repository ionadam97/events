from django.db import models
import uuid
from user.models import Profile
from egm.models import Egm
from location.models import Location


class Task(models.Model):
    STAT = (
        ('open', 'Open'),
        ('closed', 'Closed'),
        ('in_progres', 'Progres'),
        ('waiting_vnet', 'VNET'),
        ('waiting_cmac', 'CMAC'),
        ('waiting_lnm', 'LNM'),
    )
    nr = models.BigAutoField(primary_key=True, unique=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    locatia = models.ForeignKey(
        Location, null=True, blank=True, on_delete=models.DO_NOTHING)
    egm = models.ForeignKey(Egm, null=True, blank=True,
                            on_delete=models.DO_NOTHING)
    owner = models.ForeignKey(
        Profile, null=True, blank=True, on_delete=models.DO_NOTHING)
    informatorul = models.CharField(max_length=200, blank=True, null=True)
    componenta = models.ForeignKey(
        'Componenta', null=True, blank=True, on_delete=models.DO_NOTHING)
    label = models.ForeignKey(
        'Label', null=True, blank=True, on_delete=models.DO_NOTHING)
    problema = models.TextField(blank=True, null=True)
    solutie = models.TextField(blank=True, null=True)
    sumar = models.TextField(blank=True, null=True)
    responsabil = models.CharField(max_length=200, blank=True, null=True)
    rezolutie = models.ForeignKey(
        'Rezolutie', null=True, blank=True, on_delete=models.DO_NOTHING)
    status = models.CharField(max_length=200, choices=STAT, default='open')
    data_inchidere = models.DateTimeField(null=True, blank=True)
    supervisor = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return str(self.locatia.numar)

    class Meta:
        ordering = ['-created']


class Componenta(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.name


class Label(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.name


class Rezolutie(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)


    def __str__(self):
        return self.name
