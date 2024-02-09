from django.urls import reverse_lazy
from django.views.generic import CreateView
from apps.register.forms import DeportistasForm
from apps.register.models import Deportistas
class CreateDeportista(CreateView):
    model = Deportistas
    form_class= DeportistasForm
    template_name='Deportistas/RegistroDeportista.html'
    success_url = reverse_lazy('core:gracias')
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['title']='Creacion de un deportista'
        print(reverse_lazy('core:gracias'))
        return context