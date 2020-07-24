from django.shortcuts import render, HttpResponse

html_base ="""
        <h1>Mi web personal</h1>
        <ul>
            <li><a href="/">Portada</a></li>
            <li><a href="/about/">Acerca de...</a></li>
            <li><a href="/portfolio/">Portafolio</a></li>
            <li><a href="/contact/">Contacto</a></li>
        </ul>
"""

# Create your views here.
def home(request):  #Funcion para definir barra Portada  en nuestro trabajo
    return render(request, "core/home.html")

def about (request): #Funcion para definir barra Acerca de... en nuestro trabajo
    return render(request, "core/about.html")

def contact (request): #Funcion para definir barra Contacto en nuestro trabajo
    return render(request, "core/contact.html")
