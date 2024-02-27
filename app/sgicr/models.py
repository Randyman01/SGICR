from django.db import models
from django.contrib.auth.models import User


# ======================================================================================================================
# ==================================Modelos para los Nomencladores======================================================
# ======================================================================================================================


class NomAsignacion(models.Model):
    denominacion = models.CharField(max_length=30, blank=True, null=True)
    activo = models.BooleanField(default=True)


class NomCatDocente(models.Model):

    denominacion = models.CharField(max_length=30, blank=True, null=True)
    activo = models.BooleanField(default=True)


class NomCausaMovimiento (models.Model):
    denominacion = models.CharField(max_length=50, blank=True, null=True)
    activo = models.BooleanField(default=True)


class NomCiudadania (models.Model):
    denominacion = models.CharField(max_length=50, blank=True, null=True)
    activo = models.BooleanField(default=True)


class NomCondecoracion (models.Model):
    idtipocondecoracion = models.SmallIntegerField(blank=True, null=True)
    denominacion = models.CharField(max_length=50, blank=True, null=True)
    activo = models.BooleanField(default=True)

# ======================================================================================================================
# ============================== Nomencladores asociados a los Cursos ==================================================
# ======================================================================================================================


class TipoEstudios(models.Model):
    pregrado = models.BooleanField(default=False)
    otros_estudios = models.BooleanField(default=False)
    politicos = models.BooleanField(default=False)
    militares = models.BooleanField(default=False)
    activo = models.BooleanField(default=True)

    def __str__(self):
        tipos = []
        if self.pregrado:
            tipos.append('Pregrado')
        if self.otros_estudios:
            tipos.append('Otros Estudios')
        if self.politicos:
            tipos.append('Políticos')
        if self.militares:
            tipos.append('Militares')

        return ', '.join(tipos) if tipos else 'Sin tipo de estudio seleccionado'
# TipoEstudios quedaria asignando id 1-militar, 2-politicos, 3-otros estudios


class NomCursomil (models.Model):
    tipo_estudios = models.ForeignKey(TipoEstudios, on_delete=models.CASCADE, default=1)
    denominacion = models.CharField(max_length=50, blank=True, null=True)
    activo = models.BooleanField(default=True)


class NomCursopol (models.Model):
    tipo_estudios = models.ForeignKey(TipoEstudios, on_delete=models.CASCADE, default=2)
    denominacion = models.CharField(max_length=50, blank=True, null=True)
    activo = models.BooleanField(default=True)


class NomCursoesp (models.Model):  # este seria el de otros estudios
    tipo_estudios = models.ForeignKey(TipoEstudios, on_delete=models.CASCADE, default=3)
    denominacion = models.CharField(max_length=50, blank=True, null=True)
    activo = models.BooleanField(default=True)


# ======================================================================================================================
# ============================== End de Nomencladores asociados a los Cursos ===========================================
# ======================================================================================================================

class NomGrupoescolar(models.Model):
    idgrupoescolar = models.PositiveSmallIntegerField(primary_key=True)
    denominacion = models.CharField(max_length=50, blank=True, null=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.denominacion if self.denominacion else 'Sin denominación'


class NomEspecialidadpersona(models.Model):
    denominacion = models.CharField(max_length=50, blank=True, null=True)
    activo = models.BooleanField(default=True)
    idgrupoescolar = models.ForeignKey(NomGrupoescolar, on_delete=models.PROTECT, related_name='especialidades', blank=True, null=True)

    def __str__(self):
        return self.denominacion if self.denominacion else 'Sin denominación'


# ======================================================================================================================
# ===================================== Nomencladores asociados a la Salud =============================================
# ======================================================================================================================

class NomEstsalud (models.Model):
    denominacion = models.CharField(max_length=50, blank=True, null=True)
    activo = models.BooleanField(default=True)


class NomGruposanguineo (models.Model):
    denominacion = models.CharField(max_length=50, blank=True, null=True)
    activo = models.BooleanField(default=True)

 
class NomPadecimiento (models.Model):
    denominacion = models.CharField(max_length=50, blank=True, null=True)
    activo = models.BooleanField(default=True)

# ======================================================================================================================
# ============================== End de Nomencladores asociados a a la Salud ===========================================
# ======================================================================================================================

class NomExtrasocial (models.Model):
    denominacion = models.CharField(max_length=50, blank=True, null=True)
    activo = models.BooleanField(default=True)


class NomGradoCientifico (models.Model):
    denominacion = models.CharField(max_length=250)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.denominacion
 

class NomIdioma (models.Model):
    denominacion = models.CharField(max_length=50, blank=True, null=True)
    activo = models.BooleanField(default=True)

# ======================================================================================================================
# ========================= Nomencladores asociados a Armas y vehiculos ================================================
# ======================================================================================================================


class NomMarca (models.Model):
    idmarca = models.SmallIntegerField(blank=True, null=True)
    denominacion = models.CharField(max_length=50, blank=True, null=True)
    activo = models.BooleanField(default=True)
    idtipomedio = models.SmallIntegerField(blank=True, null=True)


class NomMedio (models.Model):
    denominacion_modelo = models.CharField(max_length=255, blank=True, null=True)
    idmarca = models.SmallIntegerField(blank=True, null=True)
    activo = models.BooleanField(default=True)


class NomTipomedio(models.Model):
    idtipomedio = models.SmallIntegerField(primary_key=True)
    denominacion = models.CharField(max_length=50, blank=True, null=True)
    activo = models.BooleanField(default=True)


# ======================================================================================================================
# =============================== End Nomencladores asociados a Armas y vehiculos ======================================
# ======================================================================================================================

class NomMilitancia (models.Model):
    denominacion_larga = models.CharField(max_length=30, blank=True, null=True)
    denominacion_corta = models.CharField(max_length=7, blank=True, null=True)
    activo = models.BooleanField(default=True)


class NomMotivo (models.Model):
    denominacion = models.CharField(max_length=50, blank=True, null=True)
    activo = models.BooleanField(default=True)


class NomMotivoingreso (models.Model):
    denominacion = models.CharField(max_length=50, blank=True, null=True)
    activo = models.BooleanField(default=True)


class NomMotivorelacion (models.Model):
    denominacion = models.CharField(max_length=50, blank=True, null=True)
    activo = models.BooleanField(default=True)


class NomParentesco (models.Model):
    denominacion = models.CharField(max_length=50, blank=True, null=True)
    activo = models.BooleanField(default=True)
    invfem = models.SmallIntegerField(blank=True, null=True)
    invmas = models.SmallIntegerField(blank=True, null=True)
    sexo = models.IntegerField(blank=True, null=True)
    esfamiliar = models.CharField(max_length=255, blank=True, null=True)


class NomSalida (models.Model):
    denominacion = models.CharField(max_length=50, blank=True, null=True)
    activo = models.BooleanField(default=True)

# ======================================================================================================================
# ================================Nomencladores para las Sanciones======================================================
# ======================================================================================================================


class nomTipoSancion (models.Model):
    denominacion = models.CharField(max_length=250)
    activo = models.BooleanField(default=True)


class nomSancion (models.Model):
    denominacion = models.CharField(max_length=250)
    activo = models.BooleanField(default=True)
    tipo = models.ForeignKey(nomTipoSancion, on_delete=models.PROTECT)

# ======================================================================================================================
# ==========================End Nomenclador para Sancion================================================================
# ======================================================================================================================


class NomTipoCondecoracion(models.Model):
    denominacion = models.CharField(max_length=50, blank=True, null=True)
    activo = models.BooleanField(default=True)


class NomTipoEval(models.Model):
    denominacion = models.CharField(max_length=255, blank=True, null=True)
    titulo = models.CharField(max_length=255, blank=True, null=True)
    activo = models.BooleanField(default=True)
    auto = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)


class NomTipoingreso(models.Model):
    denominacion = models.CharField(max_length=50, blank=True, null=True)
    activo = models.BooleanField(default=True)


class NomTipomoneda(models.Model):
    denominacion = models.CharField(max_length=50, blank=True, null=True)
    activo = models.BooleanField(default=True)


class NomTipoMovimiento(models.Model):
    denominacion = models.CharField(max_length=50, blank=True, null=True)
    activo = models.BooleanField(default=True)


class NomTipoPersona(models.Model):
    idtipopersona = models.AutoField(primary_key=True)
    denominacion = models.CharField(max_length=20, blank=True, null=True)


class NomPais(models.Model):
    denominacion = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self): 
        return self.denominacion

# ======================================================================================================================
# ==================================Nomencladores asociados a Direcciones===============================================
# ======================================================================================================================


class NomProvincia(models.Model):
    id_pais = models.ForeignKey(NomPais, on_delete=models.CASCADE)
    denominacion = models.CharField(max_length=50, blank=True, null=True)
 
    def __str__(self):
        return str(self.denominacion)


class NomMunicipio(models.Model):
    id_provincia = models.ForeignKey(NomProvincia, on_delete=models.CASCADE)
    id_municipio = models.IntegerField(default=1)
    denominacion = models.CharField(max_length=50, blank=True, null=True)


class NomReparto(models.Model):
    id_municipio = models.ForeignKey(NomMunicipio, on_delete=models.CASCADE)
    denominacion = models.CharField(max_length=50, blank=True, null=True) 

    def __str__(self):
        return str(self.denominacion)


# ======================================================================================================================
# ================================== End Nomencladores asociados a Direcciones==========================================
# ======================================================================================================================

class NomEstimulo(models.Model):
    denominacion = models.CharField(blank=True, null=True)


# ======================================================================================================================
# ============================ End Nomencladores sacados con inspectdb.=================================================
# ======================================================================================================================
# ================================== End Modelo para Nomencladores. ====================================================


# ======================================================================================================================
# ===================================== Modelo para Expediente. ========================================================
# ======================================================================================================================

class Persona (models.Model):
    ci= models.BigIntegerField(unique=True)
    nombre= models.CharField(max_length=250)
    primer_apellido= models.CharField(max_length=250)
    segundo_apellido= models.CharField(max_length=250)
    foto= models.ImageField(upload_to='img_expediente', blank=True, null=True)   # configurar los archivos media y static en el settings

    def __str__(self):
        return f'{self.ci}'+ " "+ self.nombre


class AnnosExpDireccion (models.Model):

    annos_administrativas = models.PositiveIntegerField()
    annos_jefe_militar = models.PositiveIntegerField()
    annos_pcc = models.PositiveIntegerField()
    annos_ujc = models.PositiveIntegerField()
    annos_org_masas = models.PositiveIntegerField()
    annos_org_populares = models.PositiveIntegerField()


class DatosPersonales (models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.PROTECT)
    sexo = models.CharField(max_length=1, choices=[
        ('F', 'Femenino'),
        ('M', 'Masculino'),
    ], default='M')
    pais = models.ForeignKey(NomPais, on_delete=models.PROTECT)
    provincia = models.ForeignKey(NomProvincia, on_delete=models.PROTECT)
    municipio = models.ForeignKey(NomMunicipio, on_delete=models.PROTECT)

    fecha_nacimiento = models.DateField(null=True, blank=True)
    edad = models.PositiveIntegerField(null=True, blank=True,editable=False)
    color_piel = models.CharField(max_length=1, choices=[
        ('1', 'Alvina'),
        ('2', 'Blanca'),
        ('3', 'Mestiza'),
        ('4', 'Negra'),
    ], default='1')
    color_ojos = models.CharField(max_length=1, choices=[
        ('1', 'Azules'),
        ('2', 'Verdes'),
        ('3', 'Pardos'),
        ('4', 'Negros'),
    ], default='1')
    color_pelo = models.CharField(max_length=1, choices=[
        ('1', 'Azul'),
        ('2', 'Verdes'),
        ('3', 'Pardos'),
        ('4', 'Negros'),
    ], default='1')
    estado_civil = models.CharField(max_length=1, choices=[
        ('1', 'Soltero'),
        ('2', 'Casado'),
        ('3', 'Divorciado'),
        ('4', 'Viudo'),
        ('5', 'No Conocido'),
    ], default='5')
    estatura = models.FloatField(null=True, blank=True)
    peso = models.FloatField(null=True, blank=True)
    telefono = models.PositiveIntegerField(null=True, blank=True)
    cat_cientifica = models.CharField(max_length=1, choices=[
        ('1', 'Aspirante a Investigador'),
        ('2', 'Investigador Agregado'),
        ('3', 'Investigador Auxiliar'),
        ('4', 'Investigador Titular'),
        ('5', 'No Conocido'),
    ], default='5')
    grado_cientifico = models.ForeignKey(NomGradoCientifico, on_delete=models.PROTECT, blank=True, null=True) #esto me da q tengo q pner un valor por default
    nivel_escolar = models.CharField(max_length=1, choices=[
        ('0', 'No Conocido'),
        ('1', 'Primaria'),
        ('2', 'Secundaria Básica'),
        ('3', 'Obrero Calificado'),
        ('4', 'Preuniversitario'),
        ('5', 'Tecnico Medio'),
        ('6', 'Universitario'),
    ], default='0')

    especialidad = models.ForeignKey(NomEspecialidadpersona, on_delete=models.PROTECT, null=True)

    # Agregar un método __str__ para mostrar información relevante en la representación de objetos
    def __str__(self):
        return f'{self.get_nivel_escolar_display()} - {self.especialidad}'

    correo = models.EmailField(null=True, blank=True)

# ======================================================================================================================
# ======================================= Modelo Integracion Revolucionaria ============================================
# ======================================================================================================================
class IntegracionRevolucionaria (models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.PROTECT, related_name='integraciones_revolucionarias')
    integracion = models.CharField(max_length=50)
    cdr = models.BooleanField(default=False)
    ctc = models.BooleanField(default=False)
    fmc = models.BooleanField(default=False)
    dc = models.BooleanField(default=False)
    acrc = models.BooleanField(default=False)
    pcc = models.BooleanField(default=False)
    fechaingreso_pcc = models.DateField(blank=True, null=True)
    ujc = models.BooleanField(default=False)
    fechaingreso_ujc = models.DateField(blank=True, null=True)
    diputado_asamblea = models.BooleanField(default=False)
    ccpcc = models.BooleanField(default=False)
    buro_politico = models.BooleanField(default=False)


class OrganismoIntegracion (models.Model):
    integracion_revolucionaria = models.ForeignKey(IntegracionRevolucionaria, on_delete=models.PROTECT)
    organismo = models.CharField(max_length=250)
    entidad = models.CharField(max_length=250)
    cargo = models.CharField(max_length=250)
    fecha_desde = models.DateField(blank=True, null=True)
    fecha_hasta = models.DateField(blank=True, null=True)

# ======================================================================================================================
# =================================== End Modelo Integracion Revolucionaria ============================================
# ======================================================================================================================



# ======================================================================================================================
# =================================== Modelo Especialidades e Idiomas ==================================================
# ======================================================================================================================
class EspecialidadPersona (models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.PROTECT)
    especialidad = models.ForeignKey(NomEspecialidadpersona, on_delete=models.PROTECT)

    # Agregar un método __str__ para mostrar información relevante en la representación de objetos
    def __str__(self):
        return f'{self.persona} - {self.especialidad}'

class IdiomaPersona (models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.PROTECT)
    idioma = models.ForeignKey(NomIdioma, on_delete=models.PROTECT)


# ======================================================================================================================
# =================================== End Modelo Especialidades e Idiomas ==============================================
# ======================================================================================================================


# ======================================================================================================================
# ========================================= Modelos para Estado de Salud. ==============================================
# ======================================================================================================================

class EstadoSalud (models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.PROTECT)
    estado = models.ForeignKey(NomEstsalud, on_delete=models.PROTECT)
    limitaciones = models.CharField(max_length=250)


class Padecimiento (models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.PROTECT)
    padecimiento = models.ForeignKey(NomPadecimiento, on_delete=models.PROTECT)
    tratamiento = models.CharField(max_length=250)

#=======================================================================================================================
# ====================================== End Modelos para Estado de Salud. =============================================
#=======================================================================================================================


#=======================================================================================================================
# ====================================== Modelo para Trayectoria Laboral. ==============================================
#=======================================================================================================================

# class TrayectoriaLaboral (models.Model):
#     persona = models.ForeignKey(Persona, on_delete=models.PROTECT)

#======================================================================================================================= 
# ====================================== End Modelo para Trayectoria Laboral. ==========================================
#=======================================================================================================================


# ======================================================================================================================
# ========================================== Modelo para Residencia. ===================================================
# ======================================================================================================================


class LugarResidencia (models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.PROTECT)
    provincia = models.ForeignKey(NomProvincia, on_delete=models.CASCADE)
    municipio = models.ForeignKey(NomMunicipio, on_delete=models.CASCADE)
    desde = models.DateField(blank=True, null=True)
    hasta = models.DateField(blank=True, null=True)
    direccion = models.CharField(max_length=250)


# ======================================================================================================================
# ========================================== End Modelo para Residencia. ===============================================
# ======================================================================================================================


# ======================================================================================================================
# ========================================== Modelo para Superacion ====================================================
# ======================================================================================================================


class Superacion (models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.PROTECT)
    tipo_estudios = models.ForeignKey(TipoEstudios, on_delete=models.PROTECT)
    centro_estudio = models.CharField(max_length=250, blank=True, null=True)
    desde = models.DateField(blank=True, null=True)
    hasta = models.DateField(blank=True, null=True)
    curso = models.CharField(blank=True, null=True)

# ======================================================================================================================
# ========================================== End Modelo para Superacion ================================================
# ======================================================================================================================


# ======================================================================================================================
# ========================================== Modelo Estancia Exterior ==================================================
# ======================================================================================================================
class EstanciaExterior (models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.PROTECT)
    tipo_salida = models.ForeignKey(NomSalida, on_delete=models.PROTECT)
    pais = models.ForeignKey(NomPais, on_delete=models.PROTECT)
    cargo = models.CharField(blank=True, null=True)
    motivo = models.ForeignKey(NomMotivo, on_delete=models.PROTECT)
    fecha_viaje = models.DateField(blank=True, null=True)

# ======================================================================================================================
# ========================================== End Modelo Estancia Exterior ==============================================
# ======================================================================================================================

# ======================================================================================================================
# ======================================== Modelo Estimulos y Sanciones ================================================
# ======================================================================================================================


class Estimulos (models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.PROTECT)
    estimulo = models.ForeignKey(NomEstimulo, on_delete=models.PROTECT)
    fecha_estimulo = models.DateField(blank=True, null=True)


class Sanciones (models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.PROTECT)
    tipo_sancion = models.ForeignKey(nomTipoSancion, on_delete=models.PROTECT)
    sancion = models.ForeignKey(nomSancion, on_delete=models.PROTECT)
    motivo_sancion = models.CharField(blank=True, null=True)
    fecha_sancion = models.DateField(blank=True, null=True)

# ======================================================================================================================
# ======================================== End Modelo Estimulos y Sanciones ============================================
# ======================================================================================================================


# ======================================================================================================================
# ======================================== Modelo Armas y Vehiculos Asignados ==========================================
# ======================================================================================================================


class MediosAsignados (models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.PROTECT)
    tipo_medio = models.ForeignKey(NomTipomedio, on_delete=models.PROTECT)
    asignacion = models.ForeignKey(NomAsignacion, on_delete=models.PROTECT)
    marca = models.ForeignKey(NomMarca, on_delete=models.PROTECT)
    modelo = models.ForeignKey(NomMedio, on_delete=models.PROTECT)
    matricula = models.CharField(blank=True, null=True)


# ======================================================================================================================
# ======================================== End Modelo Armas y Vehiculos Asignados ======================================
# ======================================================================================================================


# ======================================================================================================================
# ============================================== Modelo Datos Familiares ===============================================
# ======================================================================================================================


class DatosFamiliares (models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.PROTECT)
    parentesco = models.ForeignKey(NomParentesco, on_delete=models.PROTECT)
    allegado = models.BooleanField(blank=True, null=True)
    conviviente = models.BooleanField(blank=True, null=True)
    nombres = models.CharField(max_length=250)
    primer_apellido = models.CharField(max_length=250)
    segundo_apellido = models.CharField(max_length=250)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    organismo = models.CharField(max_length=250)
    entidad = models.CharField(max_length=250)
    cargo = models.CharField(max_length=250)
    cdr = models.BooleanField(default=False)
    ctc = models.BooleanField(default=False)
    fmc = models.BooleanField(default=False)
    dc = models.BooleanField(default=False)
    acrc = models.BooleanField(default=False)
    pcc = models.BooleanField(default=False)
    ujc = models.BooleanField(default=False)

# ======================================================================================================================
# ========================================== End Modelo Datos Familiares ===============================================
# ======================================================================================================================


# ======================================================================================================================
# ========================================== Modelo BeneficiosMonetarios ===============================================
# ======================================================================================================================
class BeneficiosMonetariosPropios (models.Model):
#    persona = models.ForeignKey(Persona, on_delete=models.PROTECT)
    tipo_ingreso = models.ForeignKey(NomTipoingreso, on_delete=models.PROTECT)
    tipo_modeda = models.ForeignKey(NomTipomoneda, on_delete=models.PROTECT)
    cuantia = models.PositiveIntegerField(blank=True, null=True)


class BeneficiosMonetariosFamiliares (models.Model):
#    persona = models.ForeignKey(Persona, on_delete=models.PROTECT)
    parentesco = models.ForeignKey(NomParentesco, on_delete=models.PROTECT)
    tipo_ingreso = models.ForeignKey(NomTipoingreso, on_delete=models.PROTECT)
    tipo_modeda = models.ForeignKey(NomTipomoneda, on_delete=models.PROTECT)


# ======================================================================================================================
# ====================================== Modelo para Trayectoria Laboral. ==============================================
# ======================================================================================================================

class NomCatCientifica:
    denominacion = models.CharField(max_length=30, blank=True, null=True)
    activo = models.BooleanField(default=True)


class NomCausaBaja:
    denominacion = models.CharField(max_length=30, blank=True, null=True)
    activo = models.BooleanField(default=True)

