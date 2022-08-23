from django.db import models
import uuid


class Egm(models.Model):
  
    serie = models.CharField(max_length=200, blank=True, null=True)
    cabinet = models.ForeignKey('Cabinet', null=True, blank=True, on_delete=models.CASCADE)
    platforma = models.ForeignKey('Platform', null=True, blank=True, on_delete=models.CASCADE)
    locatia = models.ForeignKey('Location', null=True, blank=True, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, 
                        primary_key=True, editable=False)
    def __str__(self):
        return self.serie


class Cabinet(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, 
                        primary_key=True, editable=False)

    def __str__(self):
        return self.name


class Platform(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, 
                        primary_key=True, editable=False)

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, 
                        primary_key=True, editable=False)

    def __str__(self):
        return self.name