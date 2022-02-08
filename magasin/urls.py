from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('add_magasin', views.addMagasin, name='add_produit'),
    path('update_magasin/<int:pk>', views.update_magasin, name='update_magasin'),
    path('magasin', views.MagasinView, name='magasin'),

    path('add_produit', views.addProduit, name='add_produit'),
    path('update_produit/<int:pk>', views.update_produit, name='update_produit'),
    path('produit', views.ProduitView, name='produit'),

    path('profil_magasin/<int:pk>', views.MagasinProfilView, name='profil_magasin'),

    path('profil_magasin/update_profile_magasin/<int:pk>', views.update_magasin_profil, name='profil_magasin/update_profile_magasin'),
]