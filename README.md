# Projet Django Initiatives Écologiques à Paris


![Aperçu de la page d'accueil](Goeco/static/Goeco/images/Accueil.png)

Ce projet et un site web développé avec Django et PostgreSQL qui recense différentes initiatives écologiques à Paris, comme les composteurs et les recycleries ainsi que les ressourceries.

## Objectifs du projet

- Centraliser l'information sur les lieux écoresponsables.
- Afficher la carte et les lieux associés pour chaque initiative.
- Permettre l'ajout de d'autres initiatives et villes plus tard.

## Technologies utilisées

- Python 3.12.3
- Django
- PostgreSQL
- HTML/CSS pour le front-end

## État actuel du projet

- Modèles pour les lieux créés.
- Affichage de la première initiative (Composteurs) fonctionnel. 8 composteurs disponible à titre de démonstration. Le reste des données (88 au total) seront ajouté par la suite.
- Le projet est en développement : d'autres fonctionnalités (barre de recherche, responsive ainsi que l'intégration d'API) seront ajouté plus tard.

## Installation 

bash
# Cloner le projet
git clone https://github.com/NazhaALAHYANE/autourdesoi.git
# Installer les dépendances 
pip install -r requirements.txt
# Lancer le serveur
python manage.py runserver

## Aperçu du site 

### Page des composteurs 

![Aperçu de la page des composteurs](Goeco/static/Goeco/images/Composteurs-capture1.png)

![Aperçu de la page des composteurs](Goeco/static/Goeco/images/Composteurs-capture2.png)