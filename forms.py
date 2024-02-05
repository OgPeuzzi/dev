from django import forms
from AidAuto.models import Demande, Contact, Register, login, Booking

class DemandeForm(forms.ModelForm):
    Date_Panne = forms.DateField(widget=forms.DateInput(format='%Y-%m-%d'))
    Heure_Panne = forms.TimeField(widget=forms.TimeInput(format='%H:%M'))

    class Meta:
        model = Demande
        fields = '__all__'


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"


class loginForm(forms.ModelForm):
    class Meta:
        model = login
        fields = "__all__"

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = "__all__"

class bookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = "__all__"

    SERVICE_CHOICES = [
        ('', 'Sélectionner un Service'),
        ('test_diagnostique', 'Test diagnostique'),
        ('entretien_moteur', 'Entretien du moteur'),
        ('remplacement_pneus', 'Remplacement des pneus'),
        ('changement_huile', 'Changement d\'huile')
    ]

    # Utilisez TypedChoiceField pour les choix personnalisés
    service = forms.TypedChoiceField(choices=SERVICE_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))