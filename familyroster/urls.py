from django.urls import path
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
        route='<pk>/update/',
        view=views.IndividualUpdateView.as_view(),
        name='update'
    ),
        path(
        route='<pk>/delete/',
        view=views.IndividualDeleteView.as_view(),
        name='delete'
    ),
    path(
        route='<pk>/',
        view=views.IndividualDetailView.as_view(),
        name='detail'
    ),
]
