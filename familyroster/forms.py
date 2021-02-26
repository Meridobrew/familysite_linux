from django.forms import ModelForm
from .models import Individual
fields_for_forms = {"name_last": "Фамилия", "name_first": "Имя",
              "patronym": "Отчество", "name_maiden": "Девичья фамилия", "gender": "Пол",
              "date_birth": "Дата рождения", "date_death": "Дата смерти",
              "place_birth": "Место рождения", "place_death": "Место смерти",
              "individual_notes": "Примечания"}
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