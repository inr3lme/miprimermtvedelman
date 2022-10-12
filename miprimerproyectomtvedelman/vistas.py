from django.http import HttpResponse
from django.template import context , Template

def primer_vista(request):
    return HttpResponse('<h1>Hola</h1>')

def primer_template(request):
    archivo_html = open(r'C:\Users\edelmanl\Documents\ProyectosPython\Clase_18_Django_Porfolio_Parte2\MiPrimerMTVEdelman\Templates\template.html','r')
    
    template = Template(archivo_html.read())
    
    archivo_html.close()
    
    contexto = context()
    
    template_renderizado = template.render(contexto)
    
    return HttpResponse(template_renderizado)