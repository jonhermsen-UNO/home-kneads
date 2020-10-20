from django.shortcuts import render
from django.views import generic

from .models import Animal, Species
from . import forms


def index(request):
    context = { 'page_title': 'Hello, World!' }
    return render(request, 'app/index.html', context)


class AdoptView(generic.ListView):
    template_name = 'app/adopt.html'
    context_object_name = 'adoption_list'

    def get_queryset(self):
        return Animal.objects.all().order_by('species', 'birth_date', 'name')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Adoptable Pets'
        return context


class AdoptCreate(generic.CreateView):
    template_name = 'app/adopt-edit.html'
    form_class = forms.AdoptForm
    success_url = '/adopt/'
    model = Animal

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Create Adoption Record'
        return context


class AdoptUpdate(generic.UpdateView):
    template_name = 'app/adopt-edit.html'
    form_class = forms.AdoptForm
    success_url = '/adopt/'
    model = Animal

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Update Adoption Record'
        return context
