from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

CATEGORIE = {
    (
        
        'Vehicule', (
                ('voiture', 'Voiture'),
                ('moto', 'Moto'),
                ('scooter', 'Scooter'),
                ('velo', 'Velo'),
            )
    ),
    (
        'Multimedia', (
            ('ordinateur', 'Ordinateur'),
            ('telephone', 'Telephone'),
            ('jeux', 'Jeux Videos'),
            ('television', 'Television'),
        )
    ),
    (
        'Immobilier', (
            ('electromenager', 'Electromenager'), 
            ('maison', 'Maison'), 
            ('mobilier', 'Mobilier'), 
            ('vaisselle', 'Vaisselle'),
        ),
    ),
    
    (
        'Alimentation', (
            ('animal', 'Animal'), 
            ('conserve','Conserve'), 
            ('fruits','Fruits'), 
            ('legumes','Legumes'),
        )
    ),
}

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(default='admin_app/static/images/moi.jpg')
    tel = models.IntegerField()

class Annonce(models.Model):
    titre=models.CharField(max_length=100)
    photo=models.ImageField()
    categorie=models.CharField(
        max_length=100, choices=CATEGORIE, default='Categorie')
    prix=models.IntegerField()
    description=models.TextField()
    date_ajout=models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('detail', args=[self.id])
