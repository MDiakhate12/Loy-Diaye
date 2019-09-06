from django.shortcuts import render, redirect
from admin_app.forms import *
from admin_app.models import *
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required


def connexion(request):

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        # if(User.objects.get(username=username).check_password(password)):
        if(user):
            login(request, user)
            messages.success(
                request, 'Connexion reussie ! Bienvue {}'.format(username))
            # render(request, 'admin_app/index.html', {'user':user})
            return redirect('index')
        else:
            messages.warning(
                request, "Nom d'utilisateur ou mot de passe incorrect")

    return render(request, 'admin_app/login.html', {'user': loginForm(request.POST)})


def deconnexion(request):
    logout(request)
    return redirect(reverse(connexion))


def sign_up(request):
    if request.method == 'POST':

        username = request.POST['username']
        # first_name = request.POST['first_name']
        # last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if(str(password) == str(confirm_password)):
            user = User.objects.create_user(
                username=username, email=email, password=password)
            user.save()
            return redirect('index')

    return render(request, 'admin_app/sign_up.html', {'user': UserForm(request.POST)})


def index(request):
    annonces = Annonce.objects.all()
    return render(request, 'admin_app/index.html', {'annonces': annonces})


@login_required(redirect_field_name='login')
def ajouterAnnonce(request):
    if request.method == 'POST':
        form = AnnonceForm(request.POST, request.FILES)

        
        if form.is_valid():
            # if(annonce.user.is_autenticated()):
            annonce = form.save(commit=False)
            annonce.photo = request.FILES['photo']
            annonce.user = request.user
            annonce.save()

            return redirect('index')

    form = AnnonceForm()
    return render(request, 'admin_app/create.html', {'form': form})


def afficherAnnonce(request):
    
    if(request.method == 'POST'):
        recherche = request.POST['recherche']
        annonces = Annonce.objects.filter(categorie=recherche)
        if(annonces):
            return render(request, 'admin_app/read.html', {'annonces': annonces})
        else:
            messages.warning(request, "Une telle categorie n'existe pas")
            return render(request, 'admin_app/read.html')
    else:
        annonces = Annonce.objects.all()
        return render(request, 'admin_app/read.html', {'annonces': annonces})


def supprimer(request, id):
    annonce = Annonce.objects.get(pk=id)
    annonce.delete()
    return redirect('read')


@login_required(login_url='login')
def modifier(request, id):
    if(request.user == annonce.user):
        annonce = Annonce.objects.get(pk=id)
        form = AnnonceForm(instance=annonce)
        if(request.method == 'POST') :
            form = AnnonceForm(request.POST, request.FILES, instance=annonce)
            if(form.is_valid()):
                form.save()
                return redirect('read')
        return render(request, 'admin_app/create.html', {'form': form})
    else:
        raise HttpResponse("Vous n'avez pas acces a cette page")

def orderby(request, tri):
    annonces = Annonce.objects.order_by(str(tri))
    return render(request, 'admin_app/read.html', {'annonces': annonces})

def detail(request, id):
    return render(request, 'admin_app/detail.html', {'annonce':Annonce.objects.get(pk=id)})


@login_required(login_url='login')
def profile(request, id):
    user = User.objects.get(pk=id)
    return render(request, 'admin_app/profile.html', {'annonces': user.annonce_set.all(), 'User': user})



# {% load static %}
# <!DOCTYPE html>
# <html lang="en" class="no-js">

# <head>
# 	<meta charset="UTF-8" />
# 	<meta http-equiv="X-UA-Compatible" content="IE=edge">
# 	<meta name="viewport" content="width=device-width, initial-scale=1">
# 	<title>Perspective Page View Navigation</title>
# 	<meta name="description" content="Perspective Page View Navigation: Transforms the page in 3D to reveal a menu" />
# 	<meta name="keywords"
# 		content="3d page, menu, navigation, mobile, perspective, css transform, web development, web design" />
# 	<meta name="author" content="Codrops" />
# 	<link rel="shortcut icon" href="{% static '../favicon.ico' %}">
# 	<link rel="stylesheet" type="text/css" href="{% static 'css/normalize.css' %}" />
# 	<link rel="stylesheet" type="text/css" href="{% static 'css/demo.css' %}" />
# 	<link rel="stylesheet" type="text/css" href="{% static 'css/component.css' %}" />
# 	<!-- csstransforms3d-shiv-cssclasses-prefixed-teststyles-testprop-testallprops-prefixes-domprefixes-load -->
# 	<script src="{% static 'js/modernizr.custom.25376.js' %}"></script>
# </head>

# <body>
# 	<div id="perspective" class="perspective effect-movedown">
# 		<div class="container">
# 			<div class="wrapper">
# 				<!-- wrapper needed for scroll -->
# 				<!-- Top Navigation -->
# 				<div class="codrops-top clearfix">
# 					<a class="codrops-icon codrops-icon-prev"
# 						href="http://tympanus.net/Development/ProgressButtonStyles/"><span>Left info</span></a>
# 					<span class="right"><a class="codrops-icon codrops-icon-drop"
# 							href="http://tympanus.net/codrops/?p=17915"><span>Right info</span></a></span>
# 				</div>
# 				<header class="codrops-header">
# 					<h1>Header</h1>
# 				</header>
# 				<div class="main clearfix">
# 					<div class="column">
# 						<p>Column 1</p>
# 						<p><button id="showMenu">Show Menu</button></p>
# 					</div>
# 					<div class="column">
# 						<p>Column 2</p>
# 					</div>
# 					<div class="related">
# 						Footer
# 					</div>
# 				</div><!-- /main -->
# 			</div><!-- wrapper -->
# 		</div><!-- /container -->
# 		<nav class="outer-nav top horizontal">
# 			<a href="#" class="icon-home">Home</a>
# 			<a href="#" class="icon-news">News</a>
# 			<a href="#" class="icon-image">Images</a>
# 			<a href="#" class="icon-upload">Uploads</a>
# 			<a href="#" class="icon-star">Favorites</a>
# 			<a href="#" class="icon-mail">Messages</a>
# 			<a href="#" class="icon-lock">Security</a>
# 		</nav>
# 	</div><!-- /perspective -->
# 	<script src="{% static 'js/classie.js' %}"></script>
# 	<script src="{% static 'js/menu.js' %}"></script>
# </body>

# </html>