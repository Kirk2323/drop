from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models


class serviceForm(ModelForm):
    class Meta:
        model = models.service
 
        fields = ('nom_service','date_lancement','mem','mem_vive','serveur_lancement')
        labels = {
            'nom_service':_('Nom_service'),
            'date_lancement':_('date_lancement'),
            'mem':_('mem'),
            'mem_vive':_('mem_vive'),
            'serveur':_('serveur_lancement'),
        }

class appliForm(ModelForm):
    class Meta:
        model = models.appli
        managed = False
        db_table = 'appserv_appli'
        fields = ('name_app','logo','serveur','utilisateur')
        labels = {
            'name_app':_('name_app'),
            'logo':_('logo'),
            'serveur':_('serveur'),
            'utilisateur':_('utilisateur'),
        }

class utilisateurForm(ModelForm):
    class Meta:
        model = models.utilisateur
        fields = ('nom','prenom','mail')
        labels = {
            'nom' :_('nom'),
            'prenom' :_('prenom'),
            'mail' :_('mail'),
        }

class typeForm(ModelForm):
    class Meta:
        model = models.type
        fields = ('type','description')
        labels = {
            'type' :_('type'),
            'descritpion' :_('description'),
        }

class serveurForm(ModelForm):
    class Meta:
        model = models.serveur
        fields = ('nom','type','proc','mem','stock')
        labels = {
            'nom' :_('nom'),
            'type' :_('type'),
            'proc' :_('proc'),
            'mem' :_('mem'),
            'stock' :_('stock')
        }