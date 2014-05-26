from django.views.generic import TemplateView, CreateView, ListView
from django.shortcuts 	  import render_to_response, get_object_or_404
from django.template  	  import RequestContext
from django.http      	  import HttpResponseRedirect, HttpResponse
from django.db.models     import Count, Avg
import time

from django.core.urlresolvers import reverse_lazy
from django.core.paginator    import Paginator, EmptyPage, InvalidPage

'''Librerias de Authentication '''
from django.contrib.auth 			 import login,logout,authenticate
from django.contrib.auth.models      import User
from django.contrib.auth.forms 		 import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators	 import login_required

'''Librerias App'''

from registro_estudiantes_oym.apps.home.forms      import LoginForm, sugerencias
from registro_estudiantes_oym.apps.registro.models import Estudiante, Correo, Materia, CapituloMateria, Seccion, TextoPrincipal, Profesor, Periodo, Calificacion, Grupo

def index_view(request):
    materia 	= Materia.objects.filter(id=2)        	 # Select * from materias
    cap_mat     = CapituloMateria.objects.all()
    texto   	= TextoPrincipal.objects.all()	 # Despliega el texto de la pagina principal
    seccion    	= Seccion.objects.all()
    nom_prof    = Profesor.objects.all()
    periodo     = Periodo.objects.all()
    hora        = time.time()
    ctx         = {'materia':materia, 'cap_mat':cap_mat,'texto':texto, 'seccion':seccion, 'nom_prof':nom_prof, 'hora':hora}

    return render_to_response('home/index.html',ctx,context_instance=RequestContext(request))

def login_view(request):
	#mensaje = ""
	if request.user.is_authenticated():
		return HttpResponseRedirect('/materia/')
	if request.method == "POST":
			form = LoginForm(request.POST)
			if form.is_valid():
				username = form.cleaned_data['username']
				password = form.cleaned_data['password']
				usuario  = authenticate(username=username, password=password)
				if usuario is not None and usuario.is_active:
					login(request,usuario)
					return HttpResponseRedirect('/materia/')

				else:
					return HttpResponseRedirect('/login/')
			else:
				return render_to_response('home/login.html',{'form':form},context_instance=RequestContext(request))
	else:
		form = LoginForm()
		ctx  = {'form':form}

		return render_to_response('home/login.html',ctx,context_instance=RequestContext(request))

def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/')

#@login_required(login_url = '/login/')
class RegistrarEstudiante(CreateView):
    template_name = 'home/registro_estudiantes.html'
    model = Estudiante
    success_url = reverse_lazy('vista_reg_estudiante')

'''
#Paginacion para listado estudiante
class CorreoListView(ListView):

    context_object_name = "correo"
    queryset = Correo.objects.all()
    template_name = 'home/estudiantes_registrados.html'
'''

#@login_required(login_url = '/login/')
def registrados_view(request,pagina):
	mensaje   = 'Listado estudiantes registrados'
	lista_est = Estudiante.objects.all()
	correo    = Correo.objects.all()
	grupo     = Grupo.objects.all()
	paginator = Paginator(lista_est,3)
	try:
		page = int(pagina) #Convierte la cadena de caracteres tomadas en el url a entero /1/ o /2/.
	except:
		page = 1
	try:
		estudiante = paginator.page(page)
	except (EmptyPage,InvalidPage):
		estudiante = paginator.page(paginator.num_pages)

	ctx = {'msg':mensaje, 'correo':correo, 'grupo':grupo, 'estudiante':estudiante}

	return render_to_response('home/estudiantes_registrados.html',ctx,context_instance=RequestContext(request))

@login_required(login_url = '/login/')
def sugerencias_view(request):
	enviarInfo = False
	titulo = ""
	sugerencia = ""
	if request.method == "POST":
		formulario = sugerencias(request.POST)
		if formulario.is_valid():
			enviarInfo = True
			titulo = formulario.clean_data['titulo']
			sugerencia = formulario.clean_data['sugerencia']
	else:
		formulario = buzonSugerencias()
		ctx = {'form':formulario, 'titulo':titulo, 'sugerencia':sugerencia}

		return render_to_response('home/buzon_sugerencias.html',ctx,context_instance=RequestContext(request))

@login_required(login_url = '/login/')
def cert_gallery_view(request):
	return render_to_response('home/galeria_certificados.html',context_instance=RequestContext(request))

@login_required(login_url = '/login/')
def materia_view(request):
	return render_to_response('home/seleccionar_materia.html',context_instance=RequestContext(request))

@login_required(login_url = '/login/')
def capitulos_temas_view(request):
	mensaje   = 'PROGRAMA DE ASIGNATURA'
	materia   = Materia.objects.filter(id=2)
	capitulo  = CapituloMateria.objects.values('titulo')
	num_cap   = CapituloMateria.objects.values('num_capitulo')
	cont_cap  = CapituloMateria.objects.values('contenido')
	ctx       = {'materia':materia, 'capitulo':capitulo, 'num_cap':num_cap, 'cont_cap':cont_cap, 'mensaje':mensaje}

	return render_to_response('home/indice_temas_SOII.html',ctx,context_instance=RequestContext(request))

@login_required(login_url = '/login/')
def tema_net_view(request):
	mensaje   = 'PROGRAMA DE ASIGNATURA'
	ctx       = {'mensaje':mensaje}

	return render_to_response('home/indice_tema_networking.html',ctx,context_instance=RequestContext(request))

@login_required(login_url = '/login/')
def tema_vm_view(request):
	mensaje   = 'PROGRAMA DE ASIGNATURA'
	ctx       = {'mensaje':mensaje}

	return render_to_response('home/indice_tema_virtualizacion.html',ctx,context_instance=RequestContext(request))

@login_required(login_url = '/login/')
def audiovisuales_view(request):
	return render_to_response('home/audiovisuales.html',context_instance=RequestContext(request))

@login_required(login_url = '/login/')
def rep_calificaciones_view(request):
	calificacion  = Calificacion.objects.all()
	conteo_std    = Estudiante.objects.count()
	prom_asis     = Calificacion.objects.all().aggregate(Avg('asistencia'))
	prom_prct     = Calificacion.objects.all().aggregate(Avg('pract_ind_1'))
	prom_prcl     = Calificacion.objects.all().aggregate(Avg('parcial'))
	prom_fnl      = Calificacion.objects.all().aggregate(Avg('final'))
	ctx           = {'conteo_std':conteo_std, 'prom_asis':prom_asis, 'prom_prcl':prom_prcl, 'prom_fnl':prom_fnl, 'calificacion':calificacion} 
	return render_to_response('home/reporte_calificaciones.html',ctx,context_instance=RequestContext(request))

@login_required(login_url = '/login/')
def reglamento_view(request):
	mensaje = 'Reporte Informativo'
	ctx = {'mensaje':mensaje}

	return render_to_response('home/informativo.html',ctx,context_instance=RequestContext(request))

def about_view(request):
	mensaje = 'Aplicacion de control de estudiantes...creada por Kennedy Sanchez para uso personal'
	ctx = {'msg':mensaje}

	return render_to_response('home/about.html',ctx,context_instance=RequestContext(request))

def current_datetime(request):
	hr_actual = datetime.datetime.now()
	ctx       = {'hr_actual':hr_actual}

	return render_to_response('home/index.html',ctx,context_instance=RequestContext(request))
