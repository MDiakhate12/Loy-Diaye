# Generated by Django 2.2.1 on 2019-05-12 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annonce',
            name='categorie',
            field=models.CharField(choices=[('Immobilier', (('electromenager', 'Electromenager'), ('maison', 'Maison'), ('mobilier', 'Mobilier'), ('vaisselle', 'Vaisselle'))), ('Multimedia', (('ordinateur', 'Ordinateur'), ('telephone', 'Telephone'), ('jeux', 'Jeux Videos'), ('television', 'Television'))), ('Vehicule', (('voiture', 'Voiure'), ('moto', 'Moto'), ('scooter', 'Scooter'), ('velo', 'Velo'))), ('Alimentation', (('animeaux', 'Animeaux'), ('conserve', 'Conserve'), ('fruits', 'Fruits'), ('legumes', 'Legumes')))], default='Vehicule', max_length=100),
        ),
    ]
