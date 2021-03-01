from django import forms
from django.forms import ModelForm
from .models import Individual, Relationship
fields_for_forms = {"name_last": "Фамилия", "name_first": "Имя",
                    "patronym": "Отчество", "name_maiden": "Девичья фамилия", "gender": "Пол",
                    "date_birth": "Дата рождения", "date_death": "Дата смерти",
                    "place_birth": "Место рождения", "place_death": "Место смерти",
                    "individual_notes": "Примечания"}
fields_for_forms_relationship = {"relationship_type": "Тип родства",
                                 "individual_1_id": "Выбранный человек",
                                 "individual_1_role": "Роль выбранного человека",
                                 "individual_2_role": "Роль присоединяемого человека",
                                 "individual_2_id": "Присоединяемый человек"}
class UpdateForm(ModelForm):
    class Meta:
        model = Individual
        fields = list(fields_for_forms.keys())
        labels = fields_for_forms
class CreateForm(ModelForm):
    class Meta:
        model = Individual
        fields = list(fields_for_forms.keys())
        labels = fields_for_forms

class AddRelationshipForm(ModelForm):

    individual_1_id = forms.CharField(initial=Individual.objects.get(Individual_1='15'))
    class Meta:
        model = Relationship
        fields = list(fields_for_forms_relationship.keys())
        labels = fields_for_forms_relationship
        