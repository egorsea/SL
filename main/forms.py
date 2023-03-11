from .models import *
from django import forms

# def get_unique_fields(fields_list):
    # result = []
    # for el in fields_list:
        # if el not in result:
            # result.append(el)
    # return result


class SearchForm(forms.ModelForm):
    model = Sensors
    type = forms.CharField(required=False)
    sort_field = forms.ChoiceField(
        choices=(('sensor_type', 'Name'), ('sensor_price', 'Price')),
        required=False)


class IndSearchForm(forms.Form):
    search = forms.MultipleChoiceField(
        widget=forms.SelectMultiple(attrs={'class':"form-control multiselect "}),
        label='Тип датчика', #help_text='Test',
        choices=[(sensor_type, sensor_type) for sensor_type in Sensors.objects.order_by('sensor_type').values_list('sensor_type', flat=True).distinct()],
        required=False)

    sort_by = forms.ChoiceField(
        choices=(('sensor_type', 'Тип'), ('sensor_price', 'Price')),
        required=False)


class InductiveForm(forms.Form):
    manufacturer = forms.MultipleChoiceField(
        widget=forms.SelectMultiple(attrs={'class':"form-control multiselect "}),
        label='Производитель', #help_text='Test',
        choices=[(field, field) for field in Inductive.objects.order_by('manufacturer').values_list('manufacturer', flat=True).distinct()],
        required=False)

    type = forms.MultipleChoiceField(
        widget=forms.SelectMultiple(attrs={'class':"form-control multiselect "}),
        label='Тип датчика', #help_text='Test',
        choices=[(field, field) for field in Inductive.objects.order_by('type').values_list('type', flat=True).distinct()],
        required=False)

    flush = forms.MultipleChoiceField(
        widget=forms.SelectMultiple(attrs={'class':"form-control multiselect "}),
        label='Cпособ установки', #help_text='Test',
        choices=[(field, field) for field in Inductive.objects.order_by('flush').values_list('flush', flat=True).distinct()],
        required=False)

    spec = forms.MultipleChoiceField(
        widget=forms.SelectMultiple(attrs={'class':"form-control multiselect "}),
        label='Применение', #help_text='Test',
        choices=[(field, field) for field in Inductive.objects.order_by('spec').values_list('spec', flat=True).distinct()],
        required=False)

    housing = forms.MultipleChoiceField(
        widget=forms.SelectMultiple(attrs={'class':"form-control multiselect "}),
        label='Конструктивное исполнение корпуса', #help_text='Test',
        choices=[(field, field) for field in Inductive.objects.order_by('housing').values_list('housing', flat=True).distinct()],
        required=False)

    connection = forms.MultipleChoiceField(
        widget=forms.SelectMultiple(attrs={'class':"form-control multiselect "}),
        label='Способ подключения', #help_text='Test',
        choices=[(field, field) for field in Inductive.objects.order_by('connection').values_list('connection', flat=True).distinct()],
        required=False)

    size = forms.MultipleChoiceField(
        widget=forms.SelectMultiple(attrs={'class':"form-control multiselect "}),
        label='Габарит датчика', #help_text='Test',
        choices=[(field, field) for field in Inductive.objects.order_by('size').values_list('size', flat=True).distinct()],
        required=False)

    material = forms.MultipleChoiceField(
        widget=forms.SelectMultiple(attrs={'class':"form-control multiselect "}),
        label='Материал корпуса', #help_text='Test',
        choices=[(field, field) for field in Inductive.objects.order_by('material').values_list('material', flat=True).distinct()],
        required=False)

    IP = forms.MultipleChoiceField(
        widget=forms.SelectMultiple(attrs={'class':"form-control multiselect "}),
        label='Степень защиты', #help_text='Test',
        choices=[(field, field) for field in Inductive.objects.order_by('IP').values_list('IP', flat=True).distinct()],
        required=False)

    output_structure = forms.MultipleChoiceField(
        widget=forms.SelectMultiple(attrs={'class':"form-control multiselect "}),
        label='Cтруктура выходного сигнала', #help_text='Test',
        choices=[(field, field) for field in Inductive.objects.order_by('output_structure').values_list('output_structure', flat=True).distinct()],
        required=False)

    voltage = forms.MultipleChoiceField(
        widget=forms.SelectMultiple(attrs={'class':"form-control multiselect "}),
        label='Напряжение', #help_text='Test',
        choices=[(field, field) for field in Inductive.objects.order_by('voltage').values_list('voltage', flat=True).distinct()],
        required=False)

    output_type = forms.MultipleChoiceField(
        widget=forms.SelectMultiple(attrs={'class':"form-control multiselect "}),
        label='Функция выхода', #help_text='Test',
        choices=[(field, field) for field in Inductive.objects.order_by('output_type').values_list('output_type', flat=True).distinct()],
        required=False)

    adjust = forms.MultipleChoiceField(
        widget=forms.SelectMultiple(attrs={'class':"form-control multiselect "}),
        label='Регулировка', #help_text='Test',
        choices=[(field, field) for field in Inductive.objects.order_by('adjust').values_list('adjust', flat=True).distinct()],
        required=False)

    distance = forms.MultipleChoiceField(
        widget=forms.SelectMultiple(attrs={'class':"form-control multiselect "}),
        label='Номинальное расстояние', #help_text='Test',
        choices=[(field, field) for field in Inductive.objects.order_by('distance').values_list('distance', flat=True).distinct()],
        required=False)

    indicator = forms.MultipleChoiceField(
        widget=forms.SelectMultiple(attrs={'class':"form-control multiselect "}),
        label='Индикация', #help_text='Test',
        choices=[(field, field) for field in Inductive.objects.order_by('indicator').values_list('indicator', flat=True).distinct()],
        required=False)

    temperature = forms.MultipleChoiceField(
        widget=forms.SelectMultiple(attrs={'class':"form-control multiselect "}),
        label='Температурный диапазон', #help_text='Test',
        choices=[(field, field) for field in Inductive.objects.order_by('temperature').values_list('temperature', flat=True).distinct()],
        required=False)

    # sort_by = forms.ChoiceField(
        # choices=(('name', 'name'), ('distance', 'distance'), ('price', 'price'),
                #  ('-name', '-name'), ('-distance', '-distance'), ('-price', '-price')),
        # required=False)
