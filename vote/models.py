from django.db import models

class Member(models.Model):
    Votre_nom = models.CharField(max_length=100)

    def __str__(self):
        return self.Votre_nom

# class Sondage(models.Model):
#     votant = models.OneToOneField(Member, on_delete=models.CASCADE)

    