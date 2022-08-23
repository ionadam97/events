# Generated by Django 4.1 on 2022-08-14 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['-created']},
        ),
        migrations.AlterField(
            model_name='task',
            name='solutie',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('open', 'Open'), ('closed', 'Closed'), ('in_progres', 'In progres'), ('waiting_vnet', 'Waiting for VNET'), ('waiting_cmac', 'Waiting for CMAC'), ('waiting_lnm', 'Waiting for LNM')], default='open', max_length=200),
        ),
    ]