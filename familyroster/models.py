from django.db import models
from django.urls import reverse
from autoslug import AutoSlugField

class Individual(models.Model):
    individual_id = models.AutoField
    gedcom_id = models.CharField(max_length=200, blank=True)
    name_last = models.CharField(max_length=200, default="НЕИЗВЕСТНО")
    name_first = models.CharField(max_length=200, blank=True)
    patronym = models.CharField(max_length=200, blank=True)
    name_maiden = models.CharField(max_length=200, blank=True)
    GENDER_OPTIONS = [
        ('F', 'женский'),
        ('M', 'мужской'),
        ('U', 'неизвестно'),
    ]
    gender = models.CharField(
        max_length=3,
        choices=GENDER_OPTIONS, blank=True
    )
    date_birth = models.CharField(max_length=200, blank=True)
    date_death = models.CharField(max_length=200, blank=True)
    place_birth = models.CharField(max_length=200, blank=True)
    place_death = models.CharField(max_length=200, blank=True)
    individual_notes = models.TextField(max_length=500, blank=True)
    def get_absolute_url(self):
        """Return absolute URL to the Familyroster Detail page."""
        return reverse('familyroster:detail',
            kwargs={"pk": self.pk})
'''            
class Parent(models.Model):
    individual_id = models.ForeignKey(Individual, related_name = "Child", on_delete=models.CASCADE)
    parent_individual_id = models.ForeignKey(Individual, related_name = "Parent_individual", on_delete=models.CASCADE)
    parent_type_id = models.CharField(max_length=200)
    parent_notes = models.CharField(max_length=200)
'''
class Role(models.Model):
    role_name = models.CharField(max_length=200, blank=True)

class Relationship(models.Model):
    relationship_type = models.CharField(max_length=200, blank=True)
    individual_1_id = models.ForeignKey(Individual, related_name="Individual_1", on_delete=models.CASCADE)
    individual_2_id = models.ForeignKey(Individual, related_name="Individual_2", on_delete=models.CASCADE)
    individual_1_role = models.CharField(max_length=200, blank=True)
    individual_2_role = models.CharField(max_length=200, blank=True)
    marriage_date = models.CharField(max_length=200, blank=True)