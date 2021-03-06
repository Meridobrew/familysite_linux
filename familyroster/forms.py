from django import forms
from django.forms import ModelForm
from django.http import request
from .models import Individual, Relationship
from django.urls import resolve
from django.shortcuts import render
from django.core.exceptions import ValidationError
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
    def __init__(self, *args, **kwargs):
        individual_id = kwargs.pop('individual_id', None)
        super(AddRelationshipForm,self).__init__(*args, **kwargs)
        if individual_id:
            self.fields['individual_1_id'].initial = individual_id
            #self.fields['individual_1_id'].disabled = True
    individual_1_id = forms.CharField
    class Meta:
        model = Relationship
        fields = list(fields_for_forms_relationship.keys())
        labels = fields_for_forms_relationship
    def clean(self):
        cleaned_data = super().clean()
        relationship_type = cleaned_data.get("relationship_type")
        individual_1_role = cleaned_data.get("individual_1_role")
        individual_2_role = cleaned_data.get("individual_2_role")
        if individual_1_role in ["Сестра", "Брат"] and individual_2_role in ["Сестра", "Брат"]:
            cleaned_data["relationship_type"] = "Siblings"    
        elif ((individual_1_role, individual_2_role) or (individual_2_role, individual_1_role)) in [("Отец","Дочь"), ("Отец","Сын"), ("Мать","Сын"), ("Мать","Дочь")]:
            cleaned_data["relationship_type"] = "Child-Parent"
        elif individual_1_role in ["Муж", "Жена"] and individual_2_role in ["Муж", "Жена"]:
            cleaned_data["relationship_type"] = "Marriage"
        else:
            raise ValidationError(
                    "Роли не соответствуют друг другу")
        return cleaned_data

class UpdateRelationshipForm(ModelForm):
    def __init__(self, *args, **kwargs):
        pk = kwargs.pop('pk', None)
        super(UpdateRelationshipForm,self).__init__(*args, **kwargs)
        if pk:
            self.fields['individual_1_id'].initial = pk
            self.fields['individual_1_id'].disabled = True
    individual_1_id = forms.CharField
    class Meta:
        model = Relationship
        fields = list(fields_for_forms_relationship.keys())
        labels = fields_for_forms_relationship
    def clean(self):
        cleaned_data = super().clean()
        relationship_type = cleaned_data.get("relationship_type")
        individual_1_role = cleaned_data.get("individual_1_role")
        individual_2_role = cleaned_data.get("individual_2_role")
        if individual_1_role in ["Сестра", "Брат"] and individual_2_role in ["Сестра", "Брат"]:
            cleaned_data["relationship_type"] = "Siblings"    
        elif ((individual_1_role, individual_2_role) or (individual_2_role, individual_1_role)) in [("Отец","Дочь"), ("Отец","Сын"), ("Мать","Сын"), ("Мать","Дочь")]:
            cleaned_data["relationship_type"] = "Child-Parent"
        elif individual_1_role in ["Муж", "Жена"] and individual_2_role in ["Муж", "Жена"]:
            cleaned_data["relationship_type"] = "Marriage"
        else:
            raise ValidationError(
                    "Роли не соответствуют друг другу")
        return cleaned_data
        