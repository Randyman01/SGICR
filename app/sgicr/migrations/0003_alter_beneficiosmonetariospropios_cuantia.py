# Generated by Django 5.0 on 2024-02-19 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sgicr', '0002_alter_beneficiosmonetariospropios_cuantia_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beneficiosmonetariospropios',
            name='cuantia',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]