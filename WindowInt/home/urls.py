from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('innerone/', views.innerone, name='innerone'),
    path('innertwo/', views.innertwo, name='innertwo'),
    path('innerthree/', views.innerthree, name='innerthree'),
    path('innerfour/', views.innerfour, name='innerfour'),
    path('delete/<str:fol>', views.delete, name='delete'),
    path('deleteone/<str:fol1>', views.deleteone, name='delete'),
    path('deletetwo/<str:fol2>', views.deletetwo, name='delete'),
    path('deletethree/<str:fol3>', views.deletethree, name='delete'),
    path('deletefour/<str:fol4>', views.deletefour, name='delete'),
]
