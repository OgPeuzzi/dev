from django.urls import path
from . import views # Nous avons déclarer le point(.) car nous sommes dans le même emplacement sinon on aurais écris le nom de l'app

urlpatterns = [
    path('accueil/', views.accueil, name = 'accueil'),
    path('mecanicien/', views.mecanicien, name = 'mecanicien'),
    path('about/', views.about, name = 'about'),
    path('service/', views.service, name = 'service'),
    path('demande/', views.demandeForm, name = 'demande'),
    path('contact/', views.contact, name = 'contact'),
    path('connexion/', views.connexion, name = 'connexion'),
    path('inscription/', views.inscription, name = 'inscription'),
    path('found/', views.found, name = 'found'),
    path('booking/', views.booking, name = 'booking'),
]