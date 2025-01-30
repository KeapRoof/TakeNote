# TakeNote

TakeNote est une application web permettant de prendre et sauvegarder des notes sur votre compte.

## 🛠 Technologies utilisées

- **Frontend** : Angular
- **Backend** : FastAPI
- **Base de données** : MySQL (Dockerisé)


## 🚀 Installation et exécution

### Prérequis
- [Docker](https://www.docker.com/)
- [Node.js](https://nodejs.org/) et [npm](https://www.npmjs.com/)
- [Python 3](https://www.python.org/)

### 🔧 Installation

1. **Cloner le dépôt**
   ```sh
   git clone https://github.com/KeapRoof/takenote.git
   cd takenote
   ```

2. **Lancer le projet avec Docker**
   ```sh
   cd backend
   docker-compose up -d
   ```

L'application sera accessible sur : [http://localhost:4200](http://localhost:4200)

## 📌 Fonctionnalités

- 📝 Prendre et sauvegarder des notes
- 🔐 Connexion et gestion des utilisateurs
- 📂 Organisation des notes

## 📂 Structure du projet

```
.
├── backend
│   ├── Dockerfile
│   ├── README.md
│   ├── coverage.xml
│   ├── database.py
│   ├── docker-compose.yml
│   ├── init.sql
│   ├── main.py
│   ├── models
│   │   └── models.py
│   ├── package-lock.json
│   ├── pytest.ini
│   ├── requirements.txt
│   ├── routes
│   │   ├── auth_routes.py
│   │   └── notes_routes.py
│   ├── schemas
│   │   └── schemas.py
│   ├── services
│   │   ├── auth_service.py
│   │   └── notes_service.py
│   ├── sonar-project.properties
│   ├── test_main.http
│   └── tests
│       └── unit
│           ├── auth_service_test.py
│           └── notes_service_test.py
└── frontend
    ├── Dockerfile
    ├── README.md
    ├── angular.json
    ├── nginx.conf
    ├── package-lock.json
    ├── package.json
    ├── public
    │   ├── assets
    │   │   └── add.png
    │   └── favicon.ico
    ├── server.ts
    ├── sonar-project.properties
    ├── src
    │   ├── app
    │   │   ├── app.component.css
    │   │   ├── app.component.html
    │   │   ├── app.component.spec.ts
    │   │   ├── app.component.ts
    │   │   ├── app.config.server.ts
    │   │   ├── app.config.ts
    │   │   ├── app.routes.ts
    │   │   ├── const
    │   │   │   └── noteConst.ts
    │   │   ├── interfaces
    │   │   │   ├── loginInterfaces.ts
    │   │   │   └── note.ts
    │   │   ├── pages
    │   │   │   ├── connection
    │   │   │   │   ├── connection.component.css
    │   │   │   │   ├── connection.component.html
    │   │   │   │   └── connection.component.ts
    │   │   │   ├── notes
    │   │   │   │   ├── content-note
    │   │   │   │   │   ├── content-note.component.css
    │   │   │   │   │   ├── content-note.component.html
    │   │   │   │   │   ├── content-note.component.spec.ts
    │   │   │   │   │   └── content-note.component.ts
    │   │   │   │   ├── note-page
    │   │   │   │   │   ├── note-page.component.css
    │   │   │   │   │   ├── note-page.component.html
    │   │   │   │   │   ├── note-page.component.spec.ts
    │   │   │   │   │   └── note-page.component.ts
    │   │   │   │   ├── side-list-item-note
    │   │   │   │   │   ├── side-list-item-note.component.css
    │   │   │   │   │   ├── side-list-item-note.component.html
    │   │   │   │   │   ├── side-list-item-note.component.spec.ts
    │   │   │   │   │   └── side-list-item-note.component.ts
    │   │   │   │   └── side-list-note
    │   │   │   │       ├── side-list-note.component.css
    │   │   │   │       ├── side-list-note.component.html
    │   │   │   │       ├── side-list-note.component.spec.ts
    │   │   │   │       └── side-list-note.component.ts
    │   │   │   └── signup
    │   │   │       ├── signup.component.css
    │   │   │       ├── signup.component.html
    │   │   │       ├── signup.component.spec.ts
    │   │   │       └── signup.component.ts
    │   │   └── services
    │   │       ├── auth-service.service.ts
    │   │       ├── notes.service.spec.ts
    │   │       └── notes.service.ts
    │   ├── index.html
    │   ├── main.server.ts
    │   ├── main.ts
    │   └── styles.css
    ├── tsconfig.app.json
    ├── tsconfig.json
    └── tsconfig.spec.json
```

## 👨‍💻 Auteurs

- **[Haithem](https://github.com/KeapRoof)** 
- **[Redouane](https://github.com/redoaztaz)**
- **[Jules](https://github.com/C3ll0gr4m)**
- **[Ramazan](https://github.com/Rameray1)**
