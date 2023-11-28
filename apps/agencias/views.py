from django.views.generic import ListView
from .models import Auto #para que reconozca el modelo que le paso en la class

class AutoListView(ListView):
    model = Auto
    template_name = 'agencia/auto/lista_autos.html'
    context_object_name = 'autos'
# Create your views here.
