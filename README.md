# Projet FastAPI (team hlib)

## Description

Ce projet est une API développée avec **FastAPI**, conçue pour fournir des fonctionnalités CRUD. Elle permet de gérer les différentes notes des utilisateurs, de créer de nouvelles notes et de les supprimer.  
Le projet inclut également une gestion des utilisateurs et une authentification sécurisée basée sur **JWT (JSON Web Tokens)**, tout en utilisant une base de données **MySQL**.

---

## Fonctionnalités

- Gestion des utilisateurs : création, mise à jour, suppression et récupération des données utilisateur.
- Gestion des notes : opérations CRUD complètes sur les notes associées aux utilisateurs.
- Authentification et autorisation sécurisées avec JWT.
- Intégration avec une base de données relationnelle **MySQL**.
- Déploiement via **Docker Compose** pour simplifier l'environnement de développement.

---

## Architecture du projet

- **Back-end** : Développé avec **FastAPI**, conçu pour être rapide, léger et simple à utiliser. 
- **Front-end** : Interface utilisateur développée avec  **Angular**.
- **Base de données** : Gérée avec **MySQL** pour stocker les utilisateurs et leurs notes.

---

## Prérequis

Assurez-vous d'avoir installé les éléments suivants sur votre machine :

- [Docker](https://www.docker.com/)
- [Git](https://git-scm.com/)

Vérifiez également que les ports suivants sont libres sur votre machine :

- **8000** : API FastAPI  
- **4200** : Application front-end  
- **8080** : PhpMyAdmin  
- **3306** : Base de données MySQL  

---

## Installation

1. Créez un répertoire pour héberger le projet complet (back-end et front-end) :
   ```bash
   mkdir project-hlib
   cd project-hlib
    ```

2. Clonez ce dépôt (back-end):
    ```bash
    git clone https://forge.univ-lyon1.fr/p2205078/back-end.git
    ```

3. Clonez ce dépôt (front-end):
    ```bash
    git clone https://forge.univ-lyon1.fr/p2205078/front-end_hlib.git
    ```
   
## Utilisation avec Docker

1. Assurez-vous que Docker est installé et configuré sur votre machine.

2. Se rendre dans le répertoire back-end
    ```bash
    cd back-end
    ```


3. Construisez l'image Docker :
    ```bash
    docker-compose up --build
    ```

3. L'application devrait maintenant être accessible à l'adresse [http://localhost:4200](http://localhost:4200).

## Contributeur

- Haithem HADJ-AZZEM
- Redouane AZIZI
- Ramazan KUS
- Jules VIC

