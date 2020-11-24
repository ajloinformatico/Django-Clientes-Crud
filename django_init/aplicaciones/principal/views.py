from django.shortcuts import render, redirect  # Renderiza el contenido
from .models import Persona
from .forms import Personaform


# Create your views here.

def inicio(request):
    """
    Vista para el inicio
    :param request: Petición http
    :return render: index render
    """
    personas = Persona.objects.all()  # En el editor indica que la expresión está mal pero funciona
    print(personas)
    ctx = {
        'personas': personas  # A través del diccionario envio el diccioario con los datos de la persona
    }
    # Persona.objects
    return render(request, 'index.html', ctx)  # Se le indica la petición y la plantilla


def crear(request):
    # Si la petición llega por get carge el formulario vacío
    if request.method == 'GET':
        ctx = {
            'persona_form': Personaform()
        }
    # Si la petición llega por porst
    else:
        form = Personaform(request.POST)  # DAME TODA LA INFORMACIÓN QUE VAYA VÍA POST
        # print(form)
        ctx = {
            'persona_form': form  # Carga en el contexto los datos del formulario
        }
        if form.is_valid():  # Valida automáticamente el formulario
            form.save()  # Guarda el formulario
            return redirect(
                'index')  # Redirecciona al index RECORDANDO EL NAME QUE LE PUSIMOS NO HACE FALTA PONER LA RUTA COMPLETA
    return render(request, 'crear_persona.html', ctx)


def edita(request, id):
    global ctx
    persona = Persona.objects.get(id=id)  # obtiene solo el id que sea igual al id del parámetro
    print(persona)
    if request.method == 'GET':
        form = Personaform(instance=persona)  # guarda el formulario con los valores de la persona
        # Se le pasa el formulario como contexto
        ctx = {
            'persona_form': form
        }
        # Se renderiza
    if request.method == 'POST':
        # igual que en la función de crear usuario llamamos al request de los datos por POST, pero además pasamos la instancia de
        # de persona para que no tome esta como un registro nuevo
        form = Personaform(request.POST, instance=persona)
        # El contexto lo agrego simplemente para que no hayan errores
        ctx = {
            'form': form
        }
        # Repetimos validación, guardado y redirección
        if form.is_valid():
            form.save()
            return redirect('index')

    return render(request, 'crear_persona.html', ctx)


def eliminar(request, id):
    """
    No uso ni request simplemente a partir del id cojo la persona del modelo y la elimino
    Para finalmente redireccionar a index
    :param {int} id: id del usuario
    :return {void}: simplemente elimina al usuario del recurso
    """
    persona = Persona.objects.get(id=id)
    persona.delete()
    return redirect('index')
