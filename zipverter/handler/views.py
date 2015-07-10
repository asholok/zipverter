from django.shortcuts import render
from django.views import generic
from handler.models import LoggForLocationTable


class LoggView(generic.ListView):
    model = LoggForLocationTable
    template_name = 'logs/logs.html'
    context_object_name = "logs_list"
    paginate_by = 50

    def get_queryset(self):
        return LoggForLocationTable.objects.order_by('-id')

# Create your views here.
