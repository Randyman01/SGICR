# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class EstructuraDatAgrupacionest(models.Model):
    idestructura = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)
    idagrupacion = models.SmallIntegerField(blank=True, null=True)


class EstructuraDatAgrupacionestop(models.Model):
    idestructuraop = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)
    idagrupacion = models.SmallIntegerField(blank=True, null=True)


class EstructuraDatCargo(models.Model):
    idcargo = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)
    idestructuraop = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)
    idespecialidad = models.SmallIntegerField(blank=True, null=True)
    ctp = models.SmallIntegerField(blank=True, null=True)
    ctg = models.SmallIntegerField(blank=True, null=True)
    idtipocifra = models.SmallIntegerField(blank=True, null=True)
    idprefijo = models.SmallIntegerField(blank=True, null=True)
    orden = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)
    estado = models.SmallIntegerField(blank=True, null=True)
    actual = models.CharField(max_length=255, blank=True, null=True)
    idnivelestr = models.SmallIntegerField(blank=True, null=True)
    fechaini = models.CharField(max_length=255, blank=True, null=True)
    fechafin = models.CharField(max_length=255, blank=True, null=True)
    idnomenclatura = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)


class EstructuraDatCargocivil(models.Model):
    idcargo = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)
    idcargociv = models.SmallIntegerField(blank=True, null=True)
    idcategcivil = models.SmallIntegerField(blank=True, null=True)
    salario = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)




class EstructuraDatCargomtar(models.Model):
    idcargo = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)
    idcargomilitar = models.SmallIntegerField(blank=True, null=True)
    idgradomilit = models.SmallIntegerField(blank=True, null=True)
    salario = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    escadmando = models.CharField(max_length=255, blank=True, null=True)


class EstructuraDatClasifestructura(models.Model):
    idclasificacion = models.SmallIntegerField(blank=True, null=True)
    idestructura = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)
    trial529 = models.CharField(max_length=1, blank=True, null=True)


class EstructuraDatDpa(models.Model):
    iddpa = models.IntegerField(blank=True, null=True)
    idpadre = models.IntegerField(blank=True, null=True)
    idtipodpa = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)
    fechaini = models.CharField(max_length=8, blank=True, null=True)
    fechafin = models.CharField(max_length=255, blank=True, null=True)
    cod = models.CharField(max_length=255, blank=True, null=True)
    denom = models.CharField(max_length=255, blank=True, null=True)
    nivel = models.SmallIntegerField(blank=True, null=True)
    orden = models.IntegerField(blank=True, null=True)


class EstructuraDatEntidad(models.Model):
    idestructura = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)
    idorgano = models.SmallIntegerField(blank=True, null=True)
    nroplantilla = models.CharField(max_length=8, blank=True, null=True)
    nropublico = models.CharField(max_length=255, blank=True, null=True)
    denentidad = models.CharField(max_length=150, blank=True, null=True)
    fechadirectiva = models.DateTimeField(blank=True, null=True)
    fechavigor = models.DateTimeField(blank=True, null=True)
    nrodirectiva = models.SmallIntegerField(blank=True, null=True)
    idtipocifra = models.SmallIntegerField(blank=True, null=True)
    orden = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)
    estado = models.SmallIntegerField(blank=True, null=True)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    iddpa = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)



class EstructuraDatEstructura(models.Model):
    idestructura = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)
    idpadreest = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)
    nivel = models.SmallIntegerField(blank=True, null=True)
    orden = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)
    idprefijo = models.SmallIntegerField(blank=True, null=True)
    estado = models.SmallIntegerField(blank=True, null=True)
    fechaini = models.CharField(max_length=255, blank=True, null=True)
    fechafin = models.CharField(max_length=255, blank=True, null=True)


class EstructuraDatEstructuraop(models.Model):
    idestructuraop = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)
    idpadreestop = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)
    nivel = models.SmallIntegerField(blank=True, null=True)
    orden = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)
    idprefijo = models.SmallIntegerField(blank=True, null=True)
    idestructura = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)
    estado = models.SmallIntegerField(blank=True, null=True)
    fechaini = models.CharField(max_length=255, blank=True, null=True)
    fechafin = models.CharField(max_length=255, blank=True, null=True)
    trial533 = models.CharField(max_length=1, blank=True, null=True)


class EstructuraDatMunicipio(models.Model):
    iddpa = models.IntegerField(blank=True, null=True)
    idpadre = models.IntegerField(blank=True, null=True)
    idtipodpa = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)
    cod = models.CharField(max_length=255, blank=True, null=True)
    denom = models.CharField(max_length=255, blank=True, null=True)


class EstructuraDatOrganoest(models.Model):
    idestructura = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)
    idorgano = models.SmallIntegerField(blank=True, null=True)
    nropublico = models.CharField(max_length=255, blank=True, null=True)
    denorgano = models.CharField(max_length=100, blank=True, null=True)


class EstructuraDatOrganoestop(models.Model):
    idestructuraop = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)
    idorgano = models.SmallIntegerField(blank=True, null=True)
    denorgano = models.CharField(max_length=100, blank=True, null=True)
    ctp = models.SmallIntegerField(blank=True, null=True)
    ctg = models.SmallIntegerField(blank=True, null=True)


class EstructuraDatProvincias(models.Model):
    iddpa = models.IntegerField(blank=True, null=True)
    idpadre = models.IntegerField(blank=True, null=True)
    idtipodpa = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)
    cod = models.CharField(max_length=255, blank=True, null=True)
    denom = models.CharField(max_length=255, blank=True, null=True)


class EstructuraNomAgrupacion(models.Model):
    idagrupacion = models.SmallIntegerField(blank=True, null=True)
    denagrupacion = models.CharField(max_length=60, blank=True, null=True)
    abrevagrupacion = models.CharField(max_length=15, blank=True, null=True)
    actual = models.CharField(max_length=255, blank=True, null=True)


class EstructuraNomCargocivil(models.Model):
    idcargociv = models.IntegerField(blank=True, null=True)
    dencargociv = models.CharField(max_length=60, blank=True, null=True)
    abrevcargociv = models.CharField(max_length=255, blank=True, null=True)
    idcategocup = models.SmallIntegerField(blank=True, null=True)
    actual = models.CharField(max_length=255, blank=True, null=True)


class EstructuraNomCategcivil(models.Model):
    idcategcivil = models.SmallIntegerField(blank=True, null=True)
    dencategcivil = models.CharField(max_length=20, blank=True, null=True)
    abrevcategcivil = models.CharField(max_length=10, blank=True, null=True)
    essueldo = models.CharField(max_length=255, blank=True, null=True)
    actual = models.CharField(max_length=255, blank=True, null=True)
    trial539 = models.CharField(max_length=1, blank=True, null=True)


class EstructuraNomCategocup(models.Model):
    idcategocup = models.SmallIntegerField(blank=True, null=True)
    dencategocup = models.CharField(max_length=20, blank=True, null=True)
    actual = models.CharField(max_length=255, blank=True, null=True)


class EstructuraNomClasifestructura(models.Model):
    idclasificacion = models.SmallIntegerField(blank=True, null=True)
    denomclasificacion = models.CharField(max_length=255, blank=True, null=True)
    actual = models.CharField(max_length=255, blank=True, null=True)


class EstructuraNomDpa(models.Model):
    idtipodpa = models.IntegerField(blank=True, null=True)
    denom = models.CharField(max_length=255, blank=True, null=True)
    actual = models.CharField(max_length=255, blank=True, null=True)


class EstructuraNomGradomilit(models.Model):
    idgradomilit = models.SmallIntegerField(blank=True, null=True)
    denom = models.CharField(max_length=255, blank=True, null=True)
    actual = models.CharField(max_length=255, blank=True, null=True)


class EstructuraNomNivelestr(models.Model):
    idnivelestr = models.SmallIntegerField(blank=True, null=True)
    abrevnivelestr = models.CharField(max_length=15, blank=True, null=True)
    dennivelestr = models.CharField(max_length=255, blank=True, null=True)
    actual = models.CharField(max_length=255, blank=True, null=True)


class EstructuraNomOrgano(models.Model):
    idorgano = models.SmallIntegerField(blank=True, null=True)
    denorgano = models.CharField(max_length=60, blank=True, null=True)
    abrevorgano = models.CharField(max_length=255, blank=True, null=True)
    actual = models.CharField(max_length=255, blank=True, null=True)
