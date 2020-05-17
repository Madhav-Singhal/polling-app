from django.urls import path
from . import views

urlpatterns = [
   
   path('', views.list, name = 'list'),
   path('create/', views.create, name = 'create'),
   path('view/<int:id>', views.view, name = 'view'),
   path('results/<int:id>', views.results, name = 'results'),

]