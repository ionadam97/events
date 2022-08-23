from django.db import models



class Location(models.Model):
    STAT = (
        ('deschisa', 'Deschisa'),
        ('inchisa', 'Inchisa'),
        ('in_progres', 'In progres'),
    )
    numar = models.CharField(max_length=200)
    name = models.CharField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    status = models.CharField(max_length=200, choices=STAT)
    telefon = models.CharField(max_length=200, null=True, blank=True)
    adresa_ip = models.CharField(max_length=200, null=True, blank=True)
    manager = models.ForeignKey(
        'Manager', null=True, blank=True, on_delete=models.SET_NULL)
    data_deschidere = models.DateField(null=True, blank=True)
    data_inchidere = models.DateField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)


    def __str__(self):
        return self.numar


class Manager(models.Model):
    nume = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, null=True, blank=True)
    telefon = models.CharField(max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)


    def __str__(self):
        return self.nume
