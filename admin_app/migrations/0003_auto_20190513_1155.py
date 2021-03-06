# Generated by Django 2.2.1 on 2019-05-13 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0002_auto_20190512_1916'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='annonce',
            name='photo',
        ),
        migrations.AlterField(
            model_name='annonce',
            name='categorie',
            field=models.CharField(choices=[('Immobilier', (('electromenager', 'Electromenager'), ('maison', 'Maison'), ('mobilier', 'Mobilier'), ('vaisselle', 'Vaisselle'))), ('Alimentation', (('animal', 'Animal'), ('conserve', 'Conserve'), ('fruits', 'Fruits'), ('legumes', 'Legumes'))), ('Multimedia', (('ordinateur', 'Ordinateur'), ('telephone', 'Telephone'), ('jeux', 'Jeux Videos'), ('television', 'Television'))), ('Vehicule', (('voiture', 'Voiture'), ('moto', 'Moto'), ('scooter', 'Scooter'), ('velo', 'Velo')))], default='Vehicule', max_length=100),
        ),
        migrations.AlterField(
            model_name='annonce',
            name='date_ajout',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
