# Generated by Django 2.2.1 on 2019-05-14 17:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('admin_app', '0010_auto_20190513_1744'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birthday', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('tel', models.IntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AlterField(
            model_name='annonce',
            name='categorie',
            field=models.CharField(choices=[('Vehicule', (('voiture', 'Voiture'), ('moto', 'Moto'), ('scooter', 'Scooter'), ('velo', 'Velo'))), ('Alimentation', (('animal', 'Animal'), ('conserve', 'Conserve'), ('fruits', 'Fruits'), ('legumes', 'Legumes'))), ('Immobilier', (('electromenager', 'Electromenager'), ('maison', 'Maison'), ('mobilier', 'Mobilier'), ('vaisselle', 'Vaisselle'))), ('Multimedia', (('ordinateur', 'Ordinateur'), ('telephone', 'Telephone'), ('jeux', 'Jeux Videos'), ('television', 'Television')))], default='Categorie', max_length=100),
        ),
    ]
