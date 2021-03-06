from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Individual, Relationship
from .forms import UpdateForm, CreateForm, AddRelationshipForm, UpdateRelationshipForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.db.models import F
from django.shortcuts import render

class FamilyListView(ListView):
    model = Individual

class IndividualDeleteView(LoginRequiredMixin, DeleteView):
    model = Individual
    success_url = reverse_lazy('familyroster:list')
    pk_url_kwarg = 'individual_id'

class IndividualDetailView(DetailView):
    pk_url_kwarg = 'individual_id'
    model = Individual
    def get_context_data(self, **kwargs):
        individual_id = self.kwargs.get('individual_id')
        context = super().get_context_data(**kwargs)
        q1 = Individual.objects.all().values('id', 'name_first', 'patronym', 'name_last', 'name_maiden', relative_id=F('Individual_1__individual_2_id_id'), relationship_id=F('Individual_1__id'), role=F('Individual_1__individual_1_role'))
        q2 = Individual.objects.all().values('id', 'name_first', 'patronym', 'name_last', 'name_maiden', relative_id=F('Individual_2__individual_1_id_id'), relationship_id=F('Individual_2__id'), role=F('Individual_2__individual_2_role'))
        #q3 = (q1 | q2).distinct().filter(relative_id=pk)
        context['relatif_list'] = list(q1.filter(relative_id=individual_id).distinct())+list(q2.filter(relative_id=individual_id).distinct())
        context['range'] = range(10)
        return context
fields_for_forms = {"name_last": "Фамилия", "name_first": "Имя",
                    "patronym": "Отчество", "name_maiden": "Девичья фамилия", "gender": "Пол",
                    "date_birth": "Дата рождения", "date_death": "Дата смерти",
                    "place_birth": "Место рождения", "place_death": "Место смерти",
                    "individual_notes": "Примечания"}
fields_for_forms_relationship = {"relationship_type": "Тип родства", "individual_2_id": "ID присоединяемого человека", "individual_1_role": "Роль выбранного человека", "individual_2_role": "Роль присоединяемого человека"}
class IndividualCreateView(LoginRequiredMixin, CreateView):
    model = Individual
    form_class = CreateForm
    pk_url_kwarg = 'individual_id'    
    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)
    class Meta:
        labels = fields_for_forms
class IndividualUpdateView(LoginRequiredMixin, UpdateView):
    pk_url_kwarg = 'individual_id'
    model = Individual
    form_class = UpdateForm
    action = "Update"
    class Meta:
        labels = fields_for_forms

class AddRelationship(LoginRequiredMixin, CreateView):    
    form_class = AddRelationshipForm
    labels = fields_for_forms_relationship
    model = Relationship
    def get_success_url(self):
        return reverse('familyroster:list')
    def get(self, request, *args, **kwargs):
        form = AddRelationshipForm(individual_id=kwargs.get("individual_id"))
        return render(request, 'familyroster/relationship_form.html', {'form': form})
    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

class UpdateRelationship(LoginRequiredMixin, UpdateView):    
    form_class = UpdateRelationshipForm
    labels = fields_for_forms_relationship
    pk_url_kwarg = 'relationship_id'
    model = Relationship
    action = "Update"
    def get_success_url(self):
        return reverse('familyroster:list')
    #def get(self, request, *args, **kwargs):
        #form = AddRelationshipForm(pk=kwargs.get("pk"))
        #return render(request, 'familyroster/relationship_form.html', {'form': form})
    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

class DeleteRelationship(LoginRequiredMixin, DeleteView):
    model = Relationship
    success_url = reverse_lazy('familyroster:list')
    pk_url_kwarg = 'relationship_id'