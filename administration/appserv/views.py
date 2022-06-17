from django.shortcuts import render, HttpResponseRedirect
from .forms import serviceForm
from .forms import appliForm
from .forms import utilisateurForm
from .forms import serveurForm
from .forms import typeForm
from . import models

# Create your views here.
def index(request):
    return render(request,'appserv/index.html')
def index2(request):
    return render(request,'appserv/index2.html')
def infoappli(request):
    appli = models.appli.objects.get
    return render(request,'appserv/infoappli.html',{'appli':appli})
def infoservices(request):
    services = models.service.objects.all()
    return render(request,'appserv/infoservices.html',{'services':services})
def infoserveur(request):
    serveur = models.serveur.objects.all()
    return render(request,'appserv/infoserveur.html',{'serveur':serveur})
def infoutilisateur(request):
    return render(request,'appserv/infoutilisateur.html')

def infotype(request):
    type = models.type.objects.all()
    return render(request,'appserv/infotype.html',{'type':type})

def info(request):
    return render(request,'appserv/info.html')

def ajoutservice(request):
    if request.method == "POST":
        form = serviceForm(request)
        return render(request,"appserv/ajoutservice.html",{"form" : form})
    else :
        form = serviceForm()
        return render(request, "appserv/ajoutservice.html", {"form" : form})

def ajoutappli(request):
    if request.method == "POST":
        form = appliForm(request)
        return render(request,"appserv/ajoutappli.html",{"form" : form})
    else :
        form = appliForm()
        return render(request, "appserv/ajoutappli.html", {"form" : form})

def ajouttype(request):
    if request.method == "POST":
        form = typeForm(request)
        return render(request,"appserv/ajouttype.html",{"form" : form})
    else :
        form = typeForm()
        return render(request, "appserv/ajouttype.html", {"form" : form})

def ajoutserveur(request):
    if request.method == "POST":
        form = serveurForm(request)
        return render(request,"appserv/ajoutserveur.html",{"form" : form})
    else :
        form = serveurForm()
        return render(request, "appserv/ajoutserveur.html", {"form" : form})

def ajoututilisateur(request):
    if request.method == "POST":
        form = utilisateurForm(request)
        return render(request,"appserv/ajoututilisateur.html",{"form" : form})
    else :
        form = utilisateurForm()
        return render(request, "appserv/ajoututilisateur.html", {"form" : form})

def afficheservice(request, id):
    service =models.service.objects.get( pk = id)
    return render(request,"appserv/afficheservice.html", {"service" : service})

def afficheappli(request, id):
    appli =models.appli.objects.get( pk = id)
    return render(request,"appserv/afficheappli.html", {"appli" : appli})

def afficheutilisateur(request, id):
    utils =models.utilisateur.objects.get( pk = id)
    return render(request,"appserv/afficheutilisateur.html", {"utils" : utils})

def afficheserveur(request, id):
    serveur =models.serveur.objects.get( pk = id)
    return render(request,"appserv/afficheserveur.html", {"serveur" : serveur})

def affichetype(request, id):
    type =models.type.objects.get( pk = id)
    return render(request,"appserv/affichetype.html", {"type" : type})


def traitementservice(request):
    cform = serviceForm(request.POST)
    if cform.is_valid():
        service = cform.save()
        return HttpResponseRedirect("/appserv/", {"service" : service})
    else :
        return render(request, "appserv/ajoutservice.html", {"form": cform})

def traitementappli(request):
    cform = appliForm(request.POST)
    if cform.is_valid():
        appli = cform.save()
        return HttpResponseRedirect("/appserv/", {"appli" : appli})
    else :
        return render(request, "appserv/ajoutappli.html", {"form": cform})

def traitementserveur(request):
    cform = serveurForm(request.POST)
    if cform.is_valid():
        serveur = cform.save()
        return HttpResponseRedirect("/appserv/", {"serveur" : serveur})
    else :
        return render(request, "appserv/ajoutserveur.html", {"form": cform})

def traitementutilisateur(request):
    cform = utilisateurForm(request.POST)
    if cform.is_valid():
        utilisateur = cform.save()
        return HttpResponseRedirect("/appserv/", {"utilisateur" : utilisateur})
    else :
        return render(request, "appserv/ajoututilisateur.html", {"form": cform})

def traitementtype(request):
    cform = typeForm(request.POST)
    if cform.is_valid():
        type = cform.save()
        return HttpResponseRedirect("/appserv/", {"type" : type})
    else :
        return render(request, "appserv/ajouttype.html", {"form": cform})


def updateservice(request, id):
    service = models.service.objects.get(pk=id)
    form = serviceForm(service.dico())
    return render(request,'appserv/ajoutservice.html',{'form':form, 'id':id})

def updateappli(request, id):
    appli = models.appli.objects.get(pk=id)
    form = appliForm(appli.dico())
    return render(request,'appserv/ajoutappli.html',{'form':form, 'id':id})

def updateutilisateur(request, id):
    utilisateur = models.utilisateur.objects.get(pk=id)
    form = utilisateurForm(utilisateur.dico())
    return render(request,'appserv/ajoututilisateur.html',{'form':form, 'id':id})

def updateserveur(request, id):
    serveur = models.serveur.objects.get(pk=id)
    form = serveurForm(serveur.dico())
    return render(request,'appserv/ajoutserveur.html',{'form':form, 'id':id})

def updatetype(request, id):
    type = models.type.objects.get(pk=id)
    form = typeForm(type.dico())
    return render(request,'appserv/ajouttype.html',{'form':form, 'id':id})


def updatetraitementservice(request, id):
    cform = serviceForm(request.POST)
    if cform.is_valid():
        service = cform.save(commit=False)
        service.id=id
        service.save()
        return HttpResponseRedirect("/appregion/")
    else:
        return render(request, 'appserv/ajoutservice.html', {'form': cform,"id" : id})

def updatetraitementappli(request, id):
    cform = appliForm(request.POST)
    if cform.is_valid():
        appli = cform.save(commit=False)
        appli.id=id
        appli.save()
        return HttpResponseRedirect("/appserv/")
    else:
        return render(request, 'serv/ajoutappli.html', {'form': cform,"id" : id})

def updatetraitementutilisateur(request, id):
    cform = utilisateurForm(request.POST)
    if cform.is_valid():
        utilisateur = cform.save(commit=False)
        utilisateur.id=id
        utilisateur.save()
        return HttpResponseRedirect("/appserv/")
    else:
        return render(request, 'serv/ajoututilisateur.html', {'form': cform,"id" : id})


def updatetraitementserveur(request, id):
    cform = serveurForm(request.POST)
    if cform.is_valid():
        serveur = cform.save(commit=False)
        serveur.id=id
        serveur.save()
        return HttpResponseRedirect("/appserv/")
    else:
        return render(request, 'serv/ajoutserveur.html', {'form': cform,"id" : id})


def updatetraitementtype(request, id):
    cform = typeForm(request.POST)
    if cform.is_valid():
        type = cform.save(commit=False)
        type.id=id
        type.save()
        return HttpResponseRedirect("/appserv/")
    else:
        return render(request, 'serv/ajouttype.html', {'form': cform,"id" : id})



def deleteservice(request, id):
    service = models.service.objects.get(pk=id)
    service.delete()
    return HttpResponseRedirect("/appserv/")

def deleteappli(request, id):
    appli = models.appli.objects.get(pk=id)
    appli.delete()
    return HttpResponseRedirect("/appserv/")

def deleteserveur(request, id):
    serveur = models.serveur.objects.get(pk=id)
    serveur.delete()
    return HttpResponseRedirect("/appserv/")

def deleteutilisateur(request, id):
    utilisateur = models.utilisateur.objects.get(pk=id)
    utilisateur.delete()
    return HttpResponseRedirect("/appserv/")

def deletetype(request, id):
    type = models.type.objects.get(pk=id)
    type.delete()
    return HttpResponseRedirect("/appserv/")


def show(request):
    queryset = models.appli.objects.all()
    print(queryset)
    print(len(queryset))
    return render(request, "appserv/show.html")

