from django.shortcuts import render
from .models import project

# Create your views here.
def portfolio (request): #Funcion para definir barra Portafolio en nuestro trabajo
    projects = project.objects.all() #todos los proyectos y objetos que se crean se 
                                        # colocan en la variable projects  
    return render(request, "portfolio/portfolio.html", {'projects' : projects})
                                                        # Colocamos un argumento de tipo contexto 
                                                        #  con diccionario a la lista de proyectos