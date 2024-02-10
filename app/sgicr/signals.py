from django.db.models.signals import post_migrate, post_save
from django.dispatch import receiver
from datetime import datetime

from app.sgicr.models import nomTipoSancion, nomSancion, DatosPersonales, NomCatDocente, NomGradoCientifico, \
    NomGrupoescolar


@receiver(post_migrate)
def Agregardatos(sender, **kwargs):
    if sender.name == 'app.sgicr':
        #tipo sancion
        nomTipoSancion.objects.get_or_create(denominacion ="Judiciales")
        nomTipoSancion.objects.get_or_create(denominacion ="Políticas")
        nomTipoSancion.objects.get_or_create(denominacion ="Administrativas")
        # sancion
        nomSancion.objects.get_or_create(denominacion="PENA MAXIMA",
                                         tipo=nomTipoSancion.objects.get_or_create(denominacion= "Judiciales")[0])

        # Grado Cientifico
        NomGradoCientifico.objects.get_or_create(denominacion="Maestría", activo=True)
        NomGradoCientifico.objects.get_or_create(denominacion="Especialidad", activo=True)
        NomGradoCientifico.objects.get_or_create(denominacion="Doctor en Ciencias", activo=True)
        NomGradoCientifico.objects.get_or_create(denominacion="Dr. Ciencias Físicas")
        NomGradoCientifico.objects.get_or_create(denominacion="Dr. Ciencias Matemáticas", activo=True)
        NomGradoCientifico.objects.get_or_create(denominacion="Dr. Ciencias Geológicas", activo=True)
        NomGradoCientifico.objects.get_or_create(denominacion="Dr. Ciencias Geofísicas", activo=True)
        NomGradoCientifico.objects.get_or_create(denominacion="Dr. Ciencias Quimicas", activo=True)
        NomGradoCientifico.objects.get_or_create(denominacion="Dr. Ciencias Informáticas", activo=True)
        NomGradoCientifico.objects.get_or_create(denominacion="Dr. Ciencias Geográficas", activo=True)
        NomGradoCientifico.objects.get_or_create(denominacion="Dr. Ciencias Biológicas", activo=True)
        NomGradoCientifico.objects.get_or_create(denominacion="Dr. Ciencias Farmacéuticas", activo=True)
        NomGradoCientifico.objects.get_or_create(denominacion="Dr. Ciencias Filosóficas", activo=True)
        NomGradoCientifico.objects.get_or_create(denominacion="Dr. Ciencias Sociales", activo=True)
        NomGradoCientifico.objects.get_or_create(denominacion="Dr. Ciencias Políticas", activo=True)
        NomGradoCientifico.objects.get_or_create(denominacion="Dr. Ciencias Jurídicas", activo=True)
        NomGradoCientifico.objects.get_or_create(denominacion="Dr. Ciencias Psicológicas", activo=True)
        NomGradoCientifico.objects.get_or_create(denominacion="Dr. Ciencias Históricas", activo=True)
        NomGradoCientifico.objects.get_or_create(denominacion="Dr. Ciencias Médicas", activo=True)
        NomGradoCientifico.objects.get_or_create(denominacion="Dr. Ciencias Económicas", activo=True)
        NomGradoCientifico.objects.get_or_create(denominacion="Dr. Ciencias Pedagógicas", activo=True)
        NomGradoCientifico.objects.get_or_create(denominacion="Dr. Ciencias Militares", activo=True)
        NomGradoCientifico.objects.get_or_create(denominacion="Dr. Ciencias Agrícolas", activo=True)
        NomGradoCientifico.objects.get_or_create(denominacion="Licenciado", activo=True)
        NomGradoCientifico.objects.get_or_create(denominacion="Master", activo=True)

        #Categoria Docente
        NomCatDocente.objects.get_or_create(denominacion="No Conocida", activo=True)
        NomCatDocente.objects.get_or_create(denominacion="Profesor Titular", activo=True)
        NomCatDocente.objects.get_or_create(denominacion="Asistente", activo=True)
        NomCatDocente.objects.get_or_create(denominacion="Profesor Auxiliar", activo=True)
        NomCatDocente.objects.get_or_create(denominacion="Instructor Auxiliar", activo=True)
        NomCatDocente.objects.get_or_create(denominacion="Instructor", activo=True)
        NomCatDocente.objects.get_or_create(denominacion="Auxiliar Técnico", activo=True)
        NomCatDocente.objects.get_or_create(denominacion="Profesor de Mérito", activo=True)
        NomCatDocente.objects.get_or_create(denominacion="Profesor Invitado", activo=True)
        NomCatDocente.objects.get_or_create(denominacion="Profesor Consultante", activo=True)
        NomCatDocente.objects.get_or_create(denominacion="Investigador Auxiliar", activo=True)
        NomCatDocente.objects.get_or_create(denominacion="Instructor Adjunto", activo=True)
        NomCatDocente.objects.get_or_create(denominacion="Profesor Instructor", activo=True)
        NomCatDocente.objects.get_or_create(denominacion="Profesor Adjunto", activo=True)
        NomCatDocente.objects.get_or_create(denominacion="Profesor Auxuliar Adjunto", activo=True)
        NomCatDocente.objects.get_or_create(denominacion="Profesor Principal", activo=True)
        NomCatDocente.objects.get_or_create(denominacion="Profesor Ayudante", activo=True)

        # Nivel escolar
        NomGrupoescolar.objects.get_or_create(idgrupoescolar= 0, denominacion="No Conocida", activo=True)
        NomGrupoescolar.objects.get_or_create(idgrupoescolar= 1,denominacion="Primaria", activo=True)
        NomGrupoescolar.objects.get_or_create(idgrupoescolar= 2,denominacion="Secundaria Básica", activo=True)
        NomGrupoescolar.objects.get_or_create(idgrupoescolar= 3,denominacion="Obrero Calificado", activo=True)
        NomGrupoescolar.objects.get_or_create(idgrupoescolar= 4,denominacion="Preuniversitario", activo=True)
        NomGrupoescolar.objects.get_or_create(idgrupoescolar= 5,denominacion="Técnico Medio", activo=True)
        NomGrupoescolar.objects.get_or_create(idgrupoescolar= 6,denominacion="Universitario", activo=True)


@receiver(post_save, sender=DatosPersonales)
def calcularedad(sender, instance, created, **kwargs):
    if created and instance.fecha_nacimiento:
        fechaac = datetime.now().date()
        edad = fechaac.year - instance.fecha_nacimiento.year - \
               ((fechaac.month, fechaac.day) < (instance.fecha_nacimiento.month, instance.fecha_nacimiento.day))
        instance.edad = edad
        instance.save()


