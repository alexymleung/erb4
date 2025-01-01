from django.urls import path
from . import views

urlpatterns = [
    path('<int:realtor_id>', views.realtor, name='realtor'),
]
