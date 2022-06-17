from django.db import models

class utilisateur(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    mail = models.CharField(max_length=100)

    def dico(self):
        return {'nom':self.nom,'prenom':self.prenom,'mail':self.mail}

class type(models.Model):
    type =models.CharField(max_length=200)
    description = models.TextField(blank=False)

    def dico(self):
        return {'type':self.type,'description':self.description}

class serveur(models.Model):
    nom = models.CharField(max_length=100)
    type = models.ForeignKey("type", on_delete=models.CASCADE, default=None)
    proc = models.IntegerField(blank=False)
    mem = models.IntegerField(blank=False)
    stock = models.IntegerField(blank=False)

    def dico(self):
        return {'nom':self.nom,'type de serveur':self.nom,'nombre de processeur':self.proc,'capacité mémoire':self.mem,'capacité de stockage':self.stock}


class appli(models.Model):
    name_app = models.CharField(max_length=50)
    logo = models.ImageField(blank=True)
    serveur = models.ForeignKey("serveur",on_delete=models.CASCADE, default=None)
    utilisateur = models.ForeignKey("utilisateur",on_delete=models.CASCADE, default=None)

    def dico(self):
        return {'name_app': self.name_app,'logo': self.logo, 'serveur': self.serveur, 'utilisateur':self.utilisateur}


class service(models.Model):
    nom_service = models.CharField(max_length=200)
    date_lancement = models.DateField(blank=True, null = True)
    mem = models.IntegerField(blank=False)
    mem_vive = models.IntegerField(blank=False)
    serveur_lancement =models.ForeignKey("serveur",on_delete=models.CASCADE, default=None)

    def dico(self):
        return {'nom_service': self.nom_service,'date_lancement': self.date_lancement, 'mem': self.mem, 'mem_vive':self.mem_vive,'serveur_lancement':self.serveur_lancement}


#class relation(models.Model):
    #service = models.ManyToManyField('service',through=appli)
    #appli = models.ManyToManyField('appli',through=service)
