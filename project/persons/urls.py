from django.urls import path
from .views import PersonCreateView, PersonUpdateView, PersonDeleteView, person_list

urlpatterns = [
    path('', person_list, name='person-list'),
    path('create/', PersonCreateView.as_view(), name='person-create'),
    path('<int:pk>/update/', PersonUpdateView.as_view(), name='person-update'),
    path('<int:pk>/delete/', PersonDeleteView.as_view(), name='person-delete'),
]