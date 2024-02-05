from django.db import models
from django import forms
import bcrypt
# Create your models here.



class Demande(models.Model):
    # Info demande
    Full_name = models.CharField(max_length=50)
    Statut_Demande = models.CharField(max_length=350)
    Description = models.TextField(max_length=500)
    # Info du vehicule
    marque = models.CharField(max_length=25)
    modele = models.CharField(max_length=25)
    puissance = models.CharField(max_length=25)
    energie = models.CharField(max_length=25)
    matricule = models.CharField(max_length=25)
    kilometrage = models.CharField(max_length=25)
    # Choix de la panne 
    panne = models.CharField(max_length=20)
    Date_Panne = models.DateField()
    Heure_Panne = models.TimeField()
    Lieu_Panne = models.CharField(max_length=50)



    def __str__(self):
        return self.Full_name
    
    class Meta:
        db_table = 'Demande'



class Contact(models.Model):

    First_name = models.CharField(max_length=350)
    Last_name = models.CharField(max_length=350)
    Subject = models.CharField(max_length=20, default='')
    Email = models.EmailField(max_length = 350)
    Message = models.TextField(max_length=500)

    def __str__(self):
        return self.First_name
    
    class Meta:
        db_table = 'Contact'

class Role(models.Model):

    name_role = models.CharField(max_length=20)

    def __str__(self):
        return self.name_role
    
    class Meta:
        db_table = 'Role'

class Utilisateur(models.Model):
    profession = models.ForeignKey(Role, on_delete=models.CASCADE, default='')
    first_name = models.CharField(max_length=350)
    last_name = models.CharField(max_length=350)
    région = models.CharField(max_length=350)
    num_tel = models.CharField(max_length=20)
    email = models.EmailField(max_length = 350)
    password  = models.CharField(max_length=350)
    user_image  = models.ImageField(upload_to = "Mecanicien", null = True)

    def __str__(self):
        return self.first_name
    
    class Meta:
        db_table = 'Utilisateur'

class Register(models.Model):
    first_name = models.CharField(max_length=350)
    last_name = models.CharField(max_length=350)
    email = models.EmailField(max_length=350)
    password = models.CharField(max_length=350, default='')
    confirm_password = models.CharField(max_length=350, null=True)
    
    def __str__(self):
        return self.first_name
    
    class Meta:
        db_table = 'Register'

class login(models.Model):
    username = models.CharField(max_length=350)
    password = models.CharField(max_length=350)  # Utilisez CharField pour stocker le mot de passe
    
    def __str__(self):
        return self.username
    
    class Meta:
        db_table = 'Login'

class Booking(models.Model):
    SERVICE_CHOICES = (
        ('', 'Sélectionner un Service'),
        ('test_diagnostique', 'Test diagnostique'),
        ('entretien_moteur', 'Entretien du moteur'),
        ('remplacement_pneus', 'Remplacement des pneus'),
        ('changement_huile', 'Changement d\'huile')
    )

    Full_name = models.CharField(max_length=350)
    email = models.EmailField(max_length=350)
    service = models.CharField(max_length=50, choices=SERVICE_CHOICES, default='')
    Date_reservation = models.DateField()
    Description = models.TextField(max_length=500)

    def __str__(self):
        return self.Full_name
    
    class Meta:
        db_table = 'booking'
