# Generated by Django 5.0 on 2024-02-19 13:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sgicr', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beneficiosmonetariospropios',
            name='cuantia',
            field=models.PositiveIntegerField(blank=True),
        ),
        migrations.CreateModel(
            name='BeneficiosMonetariosFamiliares',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parentesco', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sgicr.nomparentesco')),
                ('tipo_ingreso', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sgicr.nomtipoingreso')),
                ('tipo_modeda', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sgicr.nomtipomoneda')),
            ],
        ),
    ]