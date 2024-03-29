from django.urls import path
from . import views
from .views import ItemCreateView, ProduitList

urlpatterns = [
    path('', views.getRoutes, name="routes"),
    path('produits/', views.getProduits, name="produits"),
    path('produits/<str:pk>/', views.getProduit, name="produit"),
    path('send_comment/create/', ItemCreateView.as_view(), name='item-create'),
    
    path('produit-list/', ProduitList.as_view(), name='mymodel-list'),
    
    #path('recherche/', views.searchProduit, name="recherche"),
]

