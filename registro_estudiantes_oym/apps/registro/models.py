from django.db import models

class Profesor(models.Model):
	nombre           = models.CharField(max_length=45, null=False)
	apellido 		 = models.CharField(max_length=45, null=False)
	
	
	def __unicode__(self):
		nombre_profesor = "%s %s" % (self.nombre, self.apellido)
		return "%s" % (nombre_profesor)

class Titulacion(models.Model):
	certificaciones	 = models.CharField(max_length=255)
	profesion		 = models.CharField(max_length=45)

	profesor         = models.ForeignKey(Profesor)

class Grupo(models.Model):
	num_grp    		 = models.CharField(max_length=2, verbose_name='Numero de grupo')

	def __unicode__(self):
		num_grp      = "%s" % (self.num_grp)
		return "%s" 		% (num_grp)

class Estudiante(models.Model):
	SEXO 			 = (('M', 'Masculino'),('F', 'Femenino'),)	
	matricula    	 = models.CharField(max_length=12, unique=True) 
	nombre       	 = models.CharField(max_length=45)
	apellido     	 = models.CharField(max_length=45) 
	genero       	 = models.CharField(max_length=1, choices=SEXO)
	telefono     	 = models.CharField(max_length=11, null=True)
	fechareg         = models.DateTimeField(auto_now=True)
	foto        	 = models.ImageField(upload_to='images/usuarios', null=True, blank=True, verbose_name="Foto")
	
	grupo            = models.ForeignKey(Grupo)

	def __unicode__(self):
		nombre_completo = "%s %s" % (self.nombre, self.apellido)
		matricula 		= "%s"    % (self.matricula)
		return "%s >> %s"         % (nombre_completo, matricula)
    
# Este campo es necesario para registrar mas de un correo de estudiantes

class Correo(models.Model):
	correo          = models.EmailField(max_length=75, unique=True, null=True)
	estudiante      = models.ForeignKey(Estudiante, null=True, blank=True)
	profesor        = models.ForeignKey(Profesor, null=True, blank=True)

	def __unicode__(self):
		correo = "%s" % (self.correo)
		return "%s"   % (correo)

class Calificacion(models.Model):
	asistencia  	 = models.CharField(max_length=3)
	pract_ind_1      = models.CharField(max_length=3)
	pract_ind_2      = models.CharField(max_length=3)
	pract_grp_1      = models.CharField(max_length=3)
	parcial		     = models.CharField(max_length=3)
	participacion    = models.CharField(max_length=1)
	final            = models.CharField(max_length=3)
		
	estudiante       = models.ForeignKey(Estudiante)
	
	def __unicode__(self):
		asistencia   = "%s" % (self.asistencia)
		pract_ind_1  = "%s" % (self.pract_ind_1)
		pract_ind_2  = "%s" % (self.pract_ind_2)
		pract_grp_1  = "%s" % (self.pract_grp_1)
		parcial      = "%s" % (self.parcial)
		final        = "%s" % (self.final)
		#total        = int(asistencia) + int(pract_ind_1) + int(pract_ind_2) + int(pract_grp_1) + int(parcial) + int(final)
		return "%s %s %s %s %s %s" % (asistencia, pract_ind_1, pract_ind_2, pract_grp_1, parcial, final)

	def __NotaFinal__(self):
		return self.asistencia + self.pract_ind_1 + self.pract_ind_2 + self.pract_grp_1 + parcial + final
		nota_final  = property(__NotaFinal__)


class Seccion(models.Model):
	num_seccion      = models.CharField(max_length=3)

	prof             = models.ForeignKey(Profesor)

	def __unicode__(self):
		num_seccion  = "%s" % (self.num_seccion)
		return "%s"         % (num_seccion)

class Materia(models.Model):
	descripcion          = models.CharField(max_length=100)

	prof    			 = models.ForeignKey(Profesor)
	secc                 = models.ForeignKey(Seccion)

	def __unicode__(self):
		materia 	 = "%s" % (self.descripcion)
		return "%s" 		% (materia)

class CapituloMateria(models.Model):
	num_capitulo     = models.CharField(max_length="10")
	titulo           = models.CharField(max_length="50")
	contenido        = models.CharField(max_length="255")

	materia          = models.ForeignKey(Materia)

	def __unicode__(self):
		num_capitulo = "%s" % (self.num_capitulo)
		titulo       = "%s" % (self.titulo)
		contenido    = "%s" % (self.contenido)
		return "%s %s %s"   % (num_capitulo, titulo, contenido)

class Periodo(models.Model):
	fdesde			 = models.DATE_FORMAT = 'N j, Y'
	fhasta			 = models.DATE_FORMAT = 'N j, Y'

	def __unicode__(self):
	    fdesde       = "%s" % (self.fdesde)	
	    fhasta       = "%s" % (self.fhasta)	

	    return "%s %s" % (fdesde, fhasta)

class Sugerencia(models.Model):
	titulo           = models.CharField(max_length=45)
	sugerencia       = models.CharField(max_length=255)
	fechareg         = models.DateTimeField(auto_now=True)
	
	estudiante		 = models.ForeignKey(Estudiante)

	def __unicode__(self):
		titulo       = "%s" % (self.titulo)
		sugerencia   = "%s" % (self.sugerencia)

		return "%s %s" (titulo, sugerencia)


class Cuestionario(models.Model):
	#Un estudiantes muchas preguntas y respuestas
	pregunta         = models.CharField(max_length=45)
	respuesta 	     = models.CharField(max_length=255)

	estudiante		 = models.ForeignKey(Estudiante)

	def __unicode__(self):
		pregunta     = "%s" % (self.pregunta)
		respuesta    = "%s" % (self.respuesta)

		return "%s %s" (pregunta, respuesta)

class TextoPrincipal(models.Model):
	descripcion_txt  = models.TextField()

	def __unicode__(self):
		texto        = "%s" % (self.descripcion_txt)
		return "%s" % (texto)

class ReglaPuntuacion(models.Model):
	asistencia     = models.CharField(max_length=2)
	pts_trb_ind1   = models.CharField(max_length=2)
	pts_trb_ind2   = models.CharField(max_length=2)
	pts_trb_grp1   = models.CharField(max_length=2)
	parcial		   = models.CharField(max_length=2)
	exam_fnl	   = models.CharField(max_length=2)
	trab_prn       = models.CharField(max_length=7)
	trab_dig       = models.CharField(max_length=7)
	cant_pag_ind   = models.CharField(max_length=2)
	cant_pag_grp   = models.CharField(max_length=2)
	cant_preg_ind  = models.CharField(max_length=2)
	cant_preg_grp  = models.CharField(max_length=2)
	tipo_letra     = models.CharField(max_length=30) 
	tamano_letra   = models.CharField(max_length=2)
	diapositiva    = models.CharField(max_length=2)
	tiempo_estimado= models.CharField(max_length=20) 
 
'''
class SeleccionMateria(models.Model):
	uid              = models.IntegerField
	id_materia		 = models.IntegerField
	id_calif		 = models.IntegerField
	id_periodo		 = models.IntegerField
	id_seccion		 = models.IntegerField

	materia 	  	 = models.ForeignKey(Materia)
	calif            = models.ForeignKey(Calificacion)
	periodo          = models.ForeignKey(Seccion)
'''