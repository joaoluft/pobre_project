from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Person
from .forms import PersonForm

class PersonCreateView(CreateView):
    model = Person
    form_class = PersonForm
    template_name = 'person_form.html'
    success_url = reverse_lazy('person-list')

class PersonUpdateView(UpdateView):
    model = Person
    form_class = PersonForm
    template_name = 'person_form.html'
    success_url = reverse_lazy('person-list')

class PersonDeleteView(DeleteView):
    model = Person
    template_name = 'person_confirm_delete.html'
    success_url = reverse_lazy('person-list')

def person_list(request):
    people = Person.objects.all()
    return render(request, 'person_list.html', {'people': people})
