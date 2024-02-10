from django.contrib import admin
from app.sgicr.models import Persona, DatosPersonales, nomTipoSancion, NomCatDocente, NomAsignacion, NomCatCientifica, \
    NomCausaBaja, NomCausaMovimiento, NomCiudadania, NomCondecoracion, NomCursoesp, NomCursomil, \
    NomCursopol, NomEstsalud, NomExtrasocial, NomGradoCientifico, \
    NomGruposanguineo, NomIdioma, NomMarca, NomMedio, NomMilitancia, NomMotivo, NomMotivoingreso, NomMotivorelacion, \
    NomPadecimiento, NomParentesco, NomSalida, NomTipoCondecoracion, NomTipoEval, NomTipoingreso, NomTipomedio, \
    NomTipomoneda, NomTipoMovimiento, NomTipoPersona, IntegracionRevolucionaria, EspecialidadPersona, IdiomaPersona, \
    NomPais, NomProvincia, NomMunicipio, NomReparto, NomEspecialidadpersona, NomGrupoescolar, nomSancion, \
    LugarResidencia, Superacion, TipoEstudios



# Register your models here.

@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
    list_display = ('ci', 'nombre', 'primer_apellido', 'segundo_apellido')
    list_filter = ('ci',)
    search_fields = ('nombre',)


@admin.register(DatosPersonales)
class DatosPersonalesAdmin(admin.ModelAdmin):
    list_display = ('persona', 'sexo', 'pais', 'municipio', 'fecha_nacimiento', 'edad')
    # list_filter = ('ci',)
    # search_fields = ('nombre',)


@admin.register(nomTipoSancion)
class NomTipoSancionAdmin(admin.ModelAdmin):
    list_display = ('denominacion', 'activo')
    # list_filter = ('ci',)
    # search_fields = ('nombre',)



@admin.register(nomSancion)
class NomSancionAdmin(admin.ModelAdmin):
    list_display = ('denominacion', 'activo')
    # list_filter = ('ci',)
    # search_fields = ('nombre',)


@admin.register(NomCatDocente)
class NomCatDocenteAdmin(admin.ModelAdmin):
    list_display = ('denominacion', 'activo')


@admin.register(NomAsignacion)
class NomAsignacionAdmin(admin.ModelAdmin):
    list_display = ('denominacion', 'activo')


# @admin.register(NomCatCientifica)
# class nomCatCientificaAdmin(admin.ModelAdmin):
#     list_display = ('denominacion', 'activo')\



# @admin.register(NomCausaBaja)
# class nomCausaBajaAdmin(admin.ModelAdmin):
#     list_display = ('denominacion', 'activo')


@admin.register(NomCausaMovimiento)
class NomCausaMovimientoAdmin(admin.ModelAdmin):
    list_display = ('denominacion', 'activo')


@admin.register(NomCiudadania)
class NomCiudadaniaAdmin(admin.ModelAdmin):
    list_display = ('denominacion', 'activo')


@admin.register(NomCondecoracion)
class NomCondecoracionAdmin(admin.ModelAdmin):
    list_display = ('denominacion', 'activo')


@admin.register(NomCursoesp)
class NomCursoespAdmin(admin.ModelAdmin):
    list_display = ('denominacion', 'activo')


@admin.register(NomCursomil)
class NomCursomilAdmin(admin.ModelAdmin):
    list_display = ('denominacion', 'activo')


@admin.register(NomCursopol)
class NomCursopolAdmin(admin.ModelAdmin):
    list_display = ('denominacion', 'activo')


@admin.register(NomEspecialidadpersona)
class NomEspecialidadpersonaAdmin(admin.ModelAdmin):
    list_display = ('denominacion', 'activo', 'idgrupoescolar_id')


@admin.register(NomGrupoescolar)
class NomGrupoescolarAdmin(admin.ModelAdmin):
    list_display = ('idgrupoescolar', 'denominacion', 'activo')


@admin.register(NomEstsalud)
class NomEstsaludAdmin(admin.ModelAdmin):
    list_display = ('denominacion', 'activo')


@admin.register(NomExtrasocial)
class NomExtrasocialAdmin(admin.ModelAdmin):
    list_display = ('denominacion', 'activo')


@admin.register(NomGradoCientifico)
class NomGradoCientificoAdmin(admin.ModelAdmin):
    list_display = ('denominacion', 'activo')


@admin.register(NomGruposanguineo)
class NomGruposanguineoAdmin(admin.ModelAdmin):
    list_display = ('denominacion', 'activo')


@admin.register(NomIdioma)
class NomIdiomaAdmin(admin.ModelAdmin):
    list_display = ('denominacion', 'activo')


@admin.register(NomMarca)
class NomMarcaAdmin(admin.ModelAdmin):
    list_display = ('denominacion', 'idtipomedio', 'activo')


@admin.register(NomMedio)
class NomMedioAdmin(admin.ModelAdmin):
    list_display = ('denominacion_modelo', 'idmarca', 'activo')


@admin.register(NomMilitancia)
class NomMilitanciaAdmin(admin.ModelAdmin):
    list_display = ('denominacion_larga', 'denominacion_corta', 'activo')


@admin.register(NomMotivo)
class NomMotivoAdmin(admin.ModelAdmin):
    list_display = ('denominacion', 'activo')


@admin.register(NomMotivoingreso)
class NomMotivoingresoAdmin(admin.ModelAdmin):
    list_display = ('denominacion', 'activo')


@admin.register(NomMotivorelacion)
class NomMotivorelacionAdmin(admin.ModelAdmin):
    list_display = ('denominacion', 'activo')


@admin.register(NomPadecimiento)
class NomPadecimientoAdmin(admin.ModelAdmin):
    list_display = ('denominacion', 'activo')


@admin.register(NomParentesco)
class NomParentescoAdmin(admin.ModelAdmin):
    list_display = ('denominacion', 'activo')


@admin.register(NomSalida)
class NomSalidaAdmin(admin.ModelAdmin):
    list_display = ('denominacion', 'activo')


@admin.register(NomTipoCondecoracion)
class NomTipoCondecoracionAdmin(admin.ModelAdmin):
    list_display = ('denominacion', 'activo')


@admin.register(NomTipoEval)
class NomTipoEvalAdmin(admin.ModelAdmin):
    list_display = ('denominacion', 'activo')


@admin.register(NomTipoingreso)
class NomTipoingresoAdmin(admin.ModelAdmin):
    list_display = ('denominacion', 'activo')


@admin.register(NomTipomedio)
class NomTipomedioAdmin(admin.ModelAdmin):
    list_display = ('denominacion', 'activo')


@admin.register(NomTipomoneda)
class NomTipomonedaAdmin(admin.ModelAdmin):
    list_display = ('denominacion', 'activo')


@admin.register(NomTipoMovimiento)
class NomTipoMovimientoAdmin(admin.ModelAdmin):
    list_display = ('denominacion', 'activo')


@admin.register(NomTipoPersona)
class NomTipoPersonaAdmin(admin.ModelAdmin):
    list_display = ('idtipopersona', 'denominacion')



@admin.register(NomPais)
class NomPaisAdmin(admin.ModelAdmin):
    list_display = ('id', 'denominacion')


@admin.register(NomProvincia)
class NomProvinciaAdmin(admin.ModelAdmin):
    list_display = ('id', 'denominacion', 'id_pais_id')
    search_fields = ('denominacion',)


@admin.register(NomMunicipio)
class NomMunicipioAdmin(admin.ModelAdmin):
    list_display = ('id_provincia', 'id_municipio', 'denominacion')


@admin.register(NomReparto)
class NomRepartoAdmin(admin.ModelAdmin):
    list_display = ('id_municipio', 'denominacion')


@admin.register(IntegracionRevolucionaria)
class IntegracionRevolucionariaAdmin(admin.ModelAdmin):
    list_display = ('integracion', 'cdr')


# @admin.register(EspecialidadPersona)
# class EspecialidadPersonaAdmin(admin.ModelAdmin):
#     list_display = ('especialidad')
#
#
# @admin.register(IdiomaPersona)
# class IdiomaPersonaAdmin(admin.ModelAdmin):
#     list_display = ('idioma')



# @admin.register(NomPais)
# class NomPaisAdmin(admin.ModelAdmin):
#     list_display = ('id', 'denominacion')


# @admin.register(NomProvincia)
# class NomProvinciaAdmin(admin.ModelAdmin):
#     list_display = ('id', 'denominacion', 'id_pais_id')
#     search_fields = ('denominacion',)


# @admin.register(NomMunicipio)
# class NomMunicipioAdmin(admin.ModelAdmin):
#     list_display = ('id_provincia', 'denominacion')


# @admin.register(NomReparto)
# class NomRepartoAdmin(admin.ModelAdmin):
#     list_display = ('id_municipio', 'denominacion')


# @admin.register(IntegracionRevolucionaria)
# class IntegracionRevolucionariaAdmin(admin.ModelAdmin):
#     list_display = ('integracion', 'cdr')


# @admin.register(EspecialidadPersona)
# class EspecialidadPersonaAdmin(admin.ModelAdmin):
#     list_display = ('especialidad')
#
#
# @admin.register(IdiomaPersona)
# class IdiomaPersonaAdmin(admin.ModelAdmin):
#     list_display = ('idioma')


@admin.register(LugarResidencia)
class LugarResidenciaAdmin(admin.ModelAdmin):
    list_display = ('desde', 'hasta')


class SuperacionAdmin(admin.ModelAdmin):
    list_display = ('persona', 'tipo_estudios', 'centro_estudio', 'desde', 'hasta', 'curso')

    def display_tipo_estudios(self, obj):
        return obj.tipo_estudios.__str__()


admin.site.register(Superacion, SuperacionAdmin)


@admin.register(TipoEstudios)
class TipoEstudiosAdmin(admin.ModelAdmin):
    list_display = ('pregrado', 'otros_estudios', 'politicos', 'militares')