# Generated by Django 4.1 on 2022-09-05 22:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nume', models.CharField(max_length=200)),
                ('email', models.EmailField(blank=True, max_length=200, null=True)),
                ('telefon', models.CharField(blank=True, max_length=200, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numar', models.CharField(max_length=200)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('status', models.CharField(choices=[('deschisa', 'Deschisa'), ('inchisa', 'Inchisa'), ('in_progres', 'In progres')], max_length=200)),
                ('telefon', models.CharField(blank=True, max_length=200, null=True)),
                ('adresa_ip', models.CharField(blank=True, max_length=200, null=True)),
                ('data_deschidere', models.DateField(blank=True, null=True)),
                ('data_inchidere', models.DateField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('manager', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='location.manager')),
            ],
        ),
    ]
