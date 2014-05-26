from django.contrib import admin
from registro_estudiantes_oym.apps.registro.models import Estudiante, Correo, Calificacion, Materia, Periodo, TextoPrincipal, Profesor, CapituloMateria, Grupo, Seccion, Cuestionario, ReglaPuntuacion
from biblioteca.models import Libro

class EstudianteAdmin(admin.ModelAdmin):
	list_display  = ('matricula', 'nombre', 'apellido','telefono', 'genero',)
	list_filter   = ('matricula', 'nombre',)
	ordering      = ('matricula',)
	search_fields = ('matricula', 'nombre', 'apellido', 'telefono', 'genero',)

class CalificacionAdmin(admin.ModelAdmin):
	list_display  = ('asistencia', 'pract_ind_1', 'pract_ind_2', 'pract_grp_1', 'parcial', 'participacion', 'final',)
	list_editable = ('pract_ind_1', 'pract_ind_2', 'pract_grp_1', 'parcial', 'participacion', 'final',)

class ProfesorAdmin(admin.ModelAdmin):
	list_display  = ('nombre', 'apellido',)
	search_fields = ('nombre', 'apellido', 'correo',)

class CapituloMateriaAdmin(admin.ModelAdmin):
	list_display  = ('num_capitulo','titulo', 'contenido',)
	ordering      = ('num_capitulo',)
	search_fields = ('titulo', 'contenido',)

class LibroAdmin(admin.ModelAdmin):
	list_display  = ('titulo', 'autor', 'isbn', 'f_public', 'editorial', 'genero', 'website', 'port_f')
	list_filter   = ('titulo', 'isbn', 'autor', 'f_public', 'editorial', 'genero', 'website',)
	ordering      = ('titulo', 'isbn', 'autor', 'editorial', 'genero', 'website',)
	search_fields = ('titulo', 'isbn', 'autor', 'f_public', 'editorial', 'genero', 'website',)

admin.site.register(Estudiante, EstudianteAdmin),
admin.site.register(Correo),
admin.site.register(Materia),
admin.site.register(Calificacion, CalificacionAdmin),
admin.site.register(CapituloMateria, CapituloMateriaAdmin),
admin.site.register(Periodo),
admin.site.register(TextoPrincipal),
admin.site.register(Profesor, ProfesorAdmin),
admin.site.register(Grupo),
admin.site.register(Seccion),
admin.site.register(Libro, LibroAdmin),
admin.site.register(Cuestionario),
admin.site.register(ReglaPuntuacion),