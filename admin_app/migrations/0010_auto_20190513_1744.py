# Generated by Django 2.2.1 on 2019-05-13 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0009_auto_20190513_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annonce',
            name='categorie',
            field=models.CharField(choices=[('', 'Categorie'), ('Immobilier', (('electromenager', 'Electromenager'), ('maison', 'Maison'), ('mobilier', 'Mobilier'), ('vaisselle', 'Vaisselle'))), ('Multimedia', (('ordinateur', 'Ordinateur'), ('telephone', 'Telephone'), ('jeux', 'Jeux Videos'), ('television', 'Television'))), ('Vehicule', (('voiture', 'Voiture'), ('moto', 'Moto'), ('scooter', 'Scooter'), ('velo', 'Velo'))), ('Alimentation', (('animal', 'Animal'), ('conserve', 'Conserve'), ('fruits', 'Fruits'), ('legumes', 'Legumes')))], default='Categorie', max_length=100),
        ),
    ]
