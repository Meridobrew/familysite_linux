from django.urls import path, re_path
from . import views

app_name = "familyroster"
urlpatterns = [
    path(
        route='',
        view=views.FamilyListView.as_view(),
        name='list'
    ),
    path(
        route='add/',
        view=views.IndividualCreateView.as_view(),
        name='add'
    ),
    path(
        route='<int:individual_id>/update/',
        view=views.IndividualUpdateView.as_view(),
        name='update'
    ),
    path(
        route='<int:individual_id>/delete/',
        view=views.IndividualDeleteView.as_view(),
        name='delete'
    ),
    path(
        route='<int:individual_id>/add_relationship/',
        view=views.AddRelationship.as_view(),
        name='add_relationship'
    ),
    path(
        route='update_relationship/<int:relationship_id>/',
        view=views.UpdateRelationship.as_view(),
        name='update_relationship'
    ),
    path(
        route='delete_relationship/<int:relationship_id>/',
        view=views.DeleteRelationship.as_view(),
        name='delete_relationship'
    ),
    path(
        route='<int:individual_id>/',
        view=views.IndividualDetailView.as_view(),
        name='detail'
    ),
]
