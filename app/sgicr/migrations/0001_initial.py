# Generated by Django 5.0 on 2024-02-19 13:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnnosExpDireccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('annos_administrativas', models.PositiveIntegerField()),
                ('annos_jefe_militar', models.PositiveIntegerField()),
                ('annos_pcc', models.PositiveIntegerField()),
                ('annos_ujc', models.PositiveIntegerField()),
                ('annos_org_masas', models.PositiveIntegerField()),
                ('annos_org_populares', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='IntegracionRevolucionaria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('integracion', models.CharField(max_length=50)),
                ('cdr', models.BooleanField(default=False)),
                ('ctc', models.BooleanField(default=False)),
                ('fmc', models.BooleanField(default=False)),
                ('dc', models.BooleanField(default=False)),
                ('acrc', models.BooleanField(default=False)),
                ('pcc', models.BooleanField(default=False)),
                ('fechaingreso_pcc', models.DateField(blank=True, null=True)),
                ('ujc', models.BooleanField(default=False)),
                ('fechaingreso_ujc', models.DateField(blank=True, null=True)),
                ('diputado_asamblea', models.BooleanField(default=False)),
                ('ccpcc', models.BooleanField(default=False)),
                ('buro_politico', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='NomAsignacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('denominacion', models.CharField(blank=True, max_length=30, null=True)),
                ('activo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='NomCatDocente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('denominacion', models.CharField(blank=True, max_length=30, null=True)),
                ('activo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='NomCausaMovimiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('denominacion', models.CharField(blank=True, max_length=50, null=True)),
                ('activo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='NomCiudadania',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('denominacion', models.CharField(blank=True, max_length=50, null=True)),
                ('activo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='NomCondecoracion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idtipocondecoracion', models.SmallIntegerField(blank=True, null=True)),
                ('denominacion', models.CharField(blank=True, max_length=50, null=True)),
                ('activo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='NomEstimulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('denominacion', models.CharField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='NomEstsalud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('denominacion', models.CharField(blank=True, max_length=50, null=True)),
                ('activo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='NomExtrasocial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('denominacion', models.CharField(blank=True, max_length=50, null=True)),
                ('activo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='NomGradoCientifico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('denominacion', models.CharField(max_length=250)),
                ('activo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='NomGrupoescolar',
            fields=[
                ('idgrupoescolar', models.PositiveSmallIntegerField(primary_key=True, serialize=False)),
                ('denominacion', models.CharField(blank=True, max_length=50, null=True)),
                ('activo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='NomGruposanguineo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('denominacion', models.CharField(blank=True, max_length=50, null=True)),
                ('activo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='NomIdioma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('denominacion', models.CharField(blank=True, max_length=50, null=True)),
                ('activo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='NomMarca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idmarca', models.SmallIntegerField(blank=True, null=True)),
                ('denominacion', models.CharField(blank=True, max_length=50, null=True)),
                ('activo', models.BooleanField(default=True)),
                ('idtipomedio', models.SmallIntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='NomMedio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('denominacion_modelo', models.CharField(blank=True, max_length=255, null=True)),
                ('idmarca', models.SmallIntegerField(blank=True, null=True)),
                ('activo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='NomMilitancia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('denominacion_larga', models.CharField(blank=True, max_length=30, null=True)),
                ('denominacion_corta', models.CharField(blank=True, max_length=7, null=True)),
                ('activo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='NomMotivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('denominacion', models.CharField(blank=True, max_length=50, null=True)),
                ('activo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='NomMotivoingreso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('denominacion', models.CharField(blank=True, max_length=50, null=True)),
                ('activo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='NomMotivorelacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('denominacion', models.CharField(blank=True, max_length=50, null=True)),
                ('activo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='NomPadecimiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('denominacion', models.CharField(blank=True, max_length=50, null=True)),
                ('activo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='NomPais',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('denominacion', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='NomParentesco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('denominacion', models.CharField(blank=True, max_length=50, null=True)),
                ('activo', models.BooleanField(default=True)),
                ('invfem', models.SmallIntegerField(blank=True, null=True)),
                ('invmas', models.SmallIntegerField(blank=True, null=True)),
                ('sexo', models.IntegerField(blank=True, null=True)),
                ('esfamiliar', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='NomSalida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('denominacion', models.CharField(blank=True, max_length=50, null=True)),
                ('activo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='NomTipoCondecoracion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('denominacion', models.CharField(blank=True, max_length=50, null=True)),
                ('activo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='NomTipoEval',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('denominacion', models.CharField(blank=True, max_length=255, null=True)),
                ('titulo', models.CharField(blank=True, max_length=255, null=True)),
                ('activo', models.BooleanField(default=True)),
                ('auto', models.DecimalField(blank=True, decimal_places=0, max_digits=19, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='NomTipoingreso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('denominacion', models.CharField(blank=True, max_length=50, null=True)),
                ('activo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='NomTipomedio',
            fields=[
                ('idtipomedio', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('denominacion', models.CharField(blank=True, max_length=50, null=True)),
                ('activo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='NomTipomoneda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('denominacion', models.CharField(blank=True, max_length=50, null=True)),
                ('activo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='NomTipoMovimiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('denominacion', models.CharField(blank=True, max_length=50, null=True)),
                ('activo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='NomTipoPersona',
            fields=[
                ('idtipopersona', models.AutoField(primary_key=True, serialize=False)),
                ('denominacion', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='nomTipoSancion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('denominacion', models.CharField(max_length=250)),
                ('activo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ci', models.BigIntegerField(unique=True)),
                ('nombre', models.CharField(max_length=250)),
                ('primer_apellido', models.CharField(max_length=250)),
                ('segundo_apellido', models.CharField(max_length=250)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='img_expediente')),
            ],
        ),
        migrations.CreateModel(
            name='TipoEstudios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pregrado', models.BooleanField(default=False)),
                ('otros_estudios', models.BooleanField(default=False)),
                ('politicos', models.BooleanField(default=False)),
                ('militares', models.BooleanField(default=False)),
                ('activo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='NomEspecialidadpersona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('denominacion', models.CharField(blank=True, max_length=50, null=True)),
                ('activo', models.BooleanField(default=True)),
                ('idgrupoescolar', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='especialidades', to='sgicr.nomgrupoescolar')),
            ],
        ),
        migrations.CreateModel(
            name='NomProvincia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('denominacion', models.CharField(blank=True, max_length=50, null=True)),
                ('id_pais', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sgicr.nompais')),
            ],
        ),
        migrations.CreateModel(
            name='NomMunicipio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_municipio', models.IntegerField(default=1)),
                ('denominacion', models.CharField(blank=True, max_length=50, null=True)),
                ('id_provincia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sgicr.nomprovincia')),
            ],
        ),
        migrations.CreateModel(
            name='NomReparto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('denominacion', models.CharField(blank=True, max_length=50, null=True)),
                ('id_municipio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sgicr.nommunicipio')),
            ],
        ),
        migrations.CreateModel(
            name='BeneficiosMonetariosPropios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cuantia', models.PositiveIntegerField(blank=True, max_length=100, null=True)),
                ('tipo_ingreso', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sgicr.nomtipoingreso')),
                ('tipo_modeda', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sgicr.nomtipomoneda')),
            ],
        ),
        migrations.CreateModel(
            name='nomSancion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('denominacion', models.CharField(max_length=250)),
                ('activo', models.BooleanField(default=True)),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sgicr.nomtiposancion')),
            ],
        ),
        migrations.CreateModel(
            name='OrganismoIntegracion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organismo', models.CharField(max_length=250)),
                ('entidad', models.CharField(max_length=250)),
                ('cargo', models.CharField(max_length=250)),
                ('fecha_desde', models.DateField(blank=True, null=True)),
                ('fecha_hasta', models.DateField(blank=True, null=True)),
                ('integracion_revolucionaria', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sgicr.integracionrevolucionaria')),
            ],
        ),
        migrations.CreateModel(
            name='Padecimiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tratamiento', models.CharField(max_length=250)),
                ('padecimiento', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sgicr.nompadecimiento')),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sgicr.persona')),
            ],
        ),
        migrations.CreateModel(
            name='MediosAsignados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricula', models.CharField(blank=True, null=True)),
                ('asignacion', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sgicr.nomasignacion')),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sgicr.nommarca')),
                ('modelo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sgicr.nommedio')),
                ('tipo_medio', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sgicr.nomtipomedio')),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sgicr.persona')),
            ],
        ),
        migrations.CreateModel(
            name='LugarResidencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desde', models.DateField(blank=True, null=True)),
                ('hasta', models.DateField(blank=True, null=True)),
                ('direccion', models.CharField(max_length=250)),
                ('municipio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sgicr.nommunicipio')),
                ('provincia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sgicr.nomprovincia')),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sgicr.persona')),
            ],
        ),
        migrations.AddField(
            model_name='integracionrevolucionaria',
            name='persona',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='integraciones_revolucionarias', to='sgicr.persona'),
        ),
        migrations.CreateModel(
            name='IdiomaPersona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idioma', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sgicr.nomidioma')),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sgicr.persona')),
            ],
        ),
        migrations.CreateModel(
            name='Estimulos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_estimulo', models.DateField(blank=True, null=True)),
                ('estimulo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sgicr.nomestimulo')),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sgicr.persona')),
            ],
        ),
        migrations.CreateModel(
            name='EstanciaExterior',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cargo', models.CharField(blank=True, null=True)),
                ('fecha_viaje', models.DateField(blank=True, null=True)),
                ('motivo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sgicr.nommotivo')),
                ('pais', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sgicr.nompais')),
                ('tipo_salida', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sgicr.nomsalida')),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sgicr.persona')),
            ],
        ),
        migrations.CreateModel(
            name='EstadoSalud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('limitaciones', models.CharField(max_length=250)),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sgicr.nomestsalud')),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sgicr.persona')),
            ],
        ),
        migrations.CreateModel(
            name='EspecialidadPersona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('especialidad', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sgicr.nomespecialidadpersona')),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sgicr.persona')),
            ],
        ),
        migrations.CreateModel(
            name='DatosPersonales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sexo', models.CharField(choices=[('F', 'Femenino'), ('M', 'Masculino')], default='M', max_length=1)),
                ('fecha_nacimiento', models.DateField(blank=True, null=True)),
                ('edad', models.PositiveIntegerField(blank=True, editable=False, null=True)),
                ('color_piel', models.CharField(choices=[('1', 'Alvina'), ('2', 'Blanca'), ('3', 'Mestiza'), ('4', 'Negra')], default='1', max_length=1)),
                ('color_ojos', models.CharField(choices=[('1', 'Azules'), ('2', 'Verdes'), ('3', 'Pardos'), ('4', 'Negros')], default='1', max_length=1)),
                ('color_pelo', models.CharField(choices=[('1', 'Azul'), ('2', 'Verdes'), ('3', 'Pardos'), ('4', 'Negros')], default='1', max_length=1)),
                ('estado_civil', models.CharField(choices=[('1', 'Soltero'), ('2', 'Casado'), ('3', 'Divorciado'), ('4', 'Viudo'), ('5', 'No Conocido')], default='5', max_length=1)),
                ('estatura', models.FloatField(blank=True, null=True)),
                ('peso', models.FloatField(blank=True, null=True)),
                ('telefono', models.PositiveIntegerField(blank=True, null=True)),
                ('cat_cientifica', models.CharField(choices=[('1', 'Aspirante a Investigador'), ('2', 'Investigador Agregado'), ('3', 'Investigador Auxiliar'), ('4', 'Investigador Titular'), ('5', 'No Conocido')], default='5', max_length=1)),
                ('nivel_escolar', models.CharField(choices=[('0', 'No Conocido'), ('1', 'Primaria'), ('2', 'Secundaria Básica'), ('3', 'Obrero Calificado'), ('4', 'Preuniversitario'), ('5', 'Tecnico Medio'), ('6', 'Universitario')], default='0', max_length=1)),
                ('correo', models.EmailField(blank=True, max_length=254, null=True)),
                ('especialidad', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='sgicr.nomespecialidadpersona')),
                ('grado_cientifico', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='sgicr.nomgradocientifico')),
                ('municipio', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sgicr.nommunicipio')),
                ('pais', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sgicr.nompais')),
                ('provincia', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sgicr.nomprovincia')),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sgicr.persona')),
            ],
        ),
        migrations.CreateModel(
            name='DatosFamiliares',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('allegado', models.BooleanField(blank=True, null=True)),
                ('conviviente', models.BooleanField(blank=True, null=True)),
                ('nombres', models.CharField(max_length=250)),
                ('primer_apellido', models.CharField(max_length=250)),
                ('segundo_apellido', models.CharField(max_length=250)),
                ('fecha_nacimiento', models.DateField(blank=True, null=True)),
                ('organismo', models.CharField(max_length=250)),
                ('entidad', models.CharField(max_length=250)),
                ('cargo', models.CharField(max_length=250)),
                ('cdr', models.BooleanField(default=False)),
                ('ctc', models.BooleanField(default=False)),
                ('fmc', models.BooleanField(default=False)),
                ('dc', models.BooleanField(default=False)),
                ('acrc', models.BooleanField(default=False)),
                ('pcc', models.BooleanField(default=False)),
                ('ujc', models.BooleanField(default=False)),
                ('parentesco', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sgicr.nomparentesco')),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sgicr.persona')),
            ],
        ),
        migrations.CreateModel(
            name='Sanciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motivo_sancion', models.CharField(blank=True, null=True)),
                ('fecha_sancion', models.DateField(blank=True, null=True)),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sgicr.persona')),
                ('sancion', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sgicr.nomsancion')),
                ('tipo_sancion', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sgicr.nomtiposancion')),
            ],
        ),
        migrations.CreateModel(
            name='Superacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('centro_estudio', models.CharField(blank=True, max_length=250, null=True)),
                ('desde', models.DateField(blank=True, null=True)),
                ('hasta', models.DateField(blank=True, null=True)),
                ('curso', models.CharField(blank=True, null=True)),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sgicr.persona')),
                ('tipo_estudios', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sgicr.tipoestudios')),
            ],
        ),
        migrations.CreateModel(
            name='NomCursopol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('denominacion', models.CharField(blank=True, max_length=50, null=True)),
                ('activo', models.BooleanField(default=True)),
                ('tipo_estudios', models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='sgicr.tipoestudios')),
            ],
        ),
        migrations.CreateModel(
            name='NomCursomil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('denominacion', models.CharField(blank=True, max_length=50, null=True)),
                ('activo', models.BooleanField(default=True)),
                ('tipo_estudios', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='sgicr.tipoestudios')),
            ],
        ),
        migrations.CreateModel(
            name='NomCursoesp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('denominacion', models.CharField(blank=True, max_length=50, null=True)),
                ('activo', models.BooleanField(default=True)),
                ('tipo_estudios', models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to='sgicr.tipoestudios')),
            ],
        ),
    ]
