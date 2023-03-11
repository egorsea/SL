from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator

from django.views.generic.base import View
from django.views.generic import ListView
from .models import Sensors, Inductive

from .forms import SearchForm, IndSearchForm, InductiveForm
# Create your views here.
from django.db.models import Count

def index(request):
    return render (request, 'main/index.html')

def underconsruction(request):
    return render (request, 'main/optics_list.html')

def about(request):
    return render (request, 'main/about.html')

class IndSensorView(ListView):
    template = 'main/sensors_list.html'
    model = Sensors

    def dispatch(self, request, *args, **kwargs):
        self.form = IndSearchForm(request.GET)
        self.form.is_valid()
        print (self.form.cleaned_data.get('search'), self.form.cleaned_data.get('sort_by'))
        # self.search = request.GET.get('search')
        # self.sort_by = request.GET.get('sort_by')
        return super(IndSensorView, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        queryset = Sensors.objects.all()
        if self.form.cleaned_data.get('search'):
            queryset = queryset.filter(sensor_type__in = self.form.cleaned_data['search'])
        if self.form.cleaned_data.get('sort_by'):
            queryset = queryset.order_by(self.form.cleaned_data['sort_by'])
        # if self.search:
            # queryset = queryset.filter(sensor_symbol__icontains = self.search)
        # if self.sort_by:
            # queryset = queryset.order_by(self.sort_by)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(IndSensorView, self).get_context_data(**kwargs)
        context['form'] = self.form
        return context

class InductiveView(ListView):
    paginate_by = 100
    template = 'main/inductive_list.html'
    model = Inductive

    def paginate_queryset(self, queryset, page_size):
        sort_by = self.request.GET.get('sort_by', 'name')
        queryset = queryset.order_by(sort_by)
        return super().paginate_queryset(queryset, page_size)

    def dispatch(self, request, *args, **kwargs):
        # self.current_url = request.get_full_path()
        # print(current_url)
        self.form = InductiveForm(request.GET)
        self.form.is_valid()
        return super(InductiveView, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        queryset = Inductive.objects.all()
        for field_name, field in self.form.cleaned_data.items():
            if self.form.cleaned_data.get(field_name):
                queryset = queryset.filter(**{f'{field_name}__in' : field})
                # values
                #field__isnull проверка на ноль, заполнить поля другими данными
        return queryset

    def get_context_data(self, **kwargs):
        context = super(InductiveView, self).get_context_data(**kwargs)
        context['form'] = self.form
        context['current_url_parameters'] = self.request.GET.urlencode()
        return context



class SensorView(ListView):

    model = Sensors
    # template = 'main/search.html'
    def get(self, request):
        form = SearchForm()
        sensortable = Sensors.objects.all()
        return render(request, 'main/search.html', {'form': form, 'sensors_list': sensortable})


# Cсортировка выдрать из гет значения sort_field
    def dispatch(self, request, *args, **kwargs):
        self.form = SearchForm(request.GET)
        self.form.is_valid()
        return super(SensorView, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        queryset = Sensors.objects.all()
        if self.form.cleaned_data.get('type'):
            queryset = queryset.filter(sensor_type = self.form.cleaned_data['type'])
        if self.form.cleaned_data.get('sort_field'):
            queryset = queryset.order_by(self.form.cleaned_data['sort_field'])
        # print (queryset)
        return queryset

    # def get_context_data(self, **kwargs):

        # return super().get_context_data(**kwargs)
