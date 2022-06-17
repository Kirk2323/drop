from django.contrib import admin
from django.urls import path

from . import views
urlpatterns = [
    path('index/', views.index),
    path('info/', views.info),

    path('infoutilisateur/', views.infoutilisateur),
    path('ajoutservice/',views.ajoutservice),
    path('ajoutappli/',views.ajoutappli),
    path('ajoututilisateur/',views.ajoututilisateur),
    path('ajoutserveur/',views.ajoutserveur),
    path('ajouttype/',views.ajouttype),
    path('infoappli/',views.infoappli),
    path('infoservices/',views.infoservices),
    path('infoserveur/',views.infoserveur),
    path('infotype/',views.infotype),
    path('traitementservice/',views.traitementservice),
    path('traitementappli/',views.traitementappli),
    path('traitementserveur/',views.traitementserveur),
    path('traitementutilisateur/',views.traitementutilisateur),
    path('traitementtype/',views.traitementtype),
    path('',views.index2),
    path('ch/',views.index),

    path('afficheservice/<int:id>/',views.afficheservice),
    path('afficheappli/<int:id>/',views.afficheappli),
    path('afficheserveur/<int:id>/',views.afficheserveur),
    path('afficheutilisateur/<int:id>/',views.afficheutilisateur),
    path('affichetype/<int:id>/',views.affichetype),

    path('updateservice/<int:id>/',views.updateservice),
    path('updateappli/<int:id>/',views.updateappli),
    path('updateserveur/<int:id>/',views.updateserveur),
    path('updatutilisateur/<int:id>/',views.updateutilisateur),
    path('updatetype/<int:id>/',views.updatetype),


    path('updatetraitementservice/<int:id>/',views.updatetraitementservice),
    path('updatetraitementservice//', views.updatetraitementservice),


    path('updatetraitementappli/<int:id>/',views.updatetraitementappli),
    path('updatetraitementserveur/<int:id>/',views.updatetraitementserveur),
    path('updatetraitementutilisateur/<int:id>/',views.updatetraitementutilisateur),
    path('updatetraitementtype/<int:id>/',views.updatetraitementtype),


    path('deleteservice/<int:id>/',views.deleteservice),
    path('deleteappli/<int:id>/',views.deleteappli),
    path('deleteserveur/<int:id>/',views.deleteserveur),
    path('deleteutilisateur/<int:id>/',views.deleteutilisateur),
    path('deletetype/<int:id>/',views.deletetype),
    path("show/", views.show),


]
