from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import *
from apps.register.forms import DeportistasForm
from apps.core.mixins import ValidatePermissionRequiredMixin
from apps.register.models import *
from django.core import serializers
import json

class DeportistasListView(LoginRequiredMixin, ValidatePermissionRequiredMixin, ListView):
    model = Deportistas
    template_name = 'deportistas/list.html'
    permission_required = 'app.view_deportistas'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
  
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                position = 1
                for i in Deportistas.objects.all():
                    item = i.toJSON()
                    item['position'] = position
                    data.append(item)
                    position+=1
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado áreas de Deportistas'
        context['list_url'] = reverse_lazy('core:Deportistas_list')
        context['create_url'] = reverse_lazy('core:Dashboard')
        context['entity'] = 'Deportistas'
        return context