from django.urls import path
from .views import contact_list, delete_contact

urlpatterns = [
    path('', contact_list, name='contact_list'),
    path('delete/<int:contact_id>/', delete_contact, name='delete_contact'),
]