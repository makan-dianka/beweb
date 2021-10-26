from django.db import models

class Member(models.Model):
    nom_de_candidat = models.CharField(max_length=100)
    def __str__(self):
        return self.nom_de_candidat

class Sondage(models.Model):
    votre_nom = models.CharField(max_length=255, default='')
    candidats = models.ForeignKey(Member, on_delete=models.CASCADE)  
    def __str__(self):
        return f"{self.votre_nom} | {self.candidats}"