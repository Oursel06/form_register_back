# Form Register Backend - FastAPI + MySQL

Ce projet est une API backend développée avec **FastAPI** et connectée à une base de données **MySQL**, contenant une interface d'administration via **Adminer**. Il est prêt à être exécuté localement avec **Docker**, et automatiquement déployé sur **Vercel** grâce à un pipeline CI/CD.

### Prérequis

Avant de commencer, assurez-vous d'avoir installé :
- [Docker & Docker Compose](https://docs.docker.com/get-docker/)
- [Git](https://git-scm.com/)
- (Facultatif) Un client HTTP comme [Postman](https://www.postman.com/) ou [Insomnia](https://insomnia.rest/)

---

### Cloner le dépôt

```bash
git clone <url-du-repo>
cd <nom-du-dossier>
```

### Lancer les conteneurs Docker

Démarrez l’environnement de développement local avec Docker :

```bash
docker-compose up --build
```

Ce script va :
- Construire l'image Docker du backend  
- Démarrer la base de données MySQL  
- Exécuter le script d'initialisation scripts/init_db.py
- Lancer le serveur FastAPI sur le port 8000

### Accéder à l’API (Swagger UI)

Une fois le backend lancé, accédez à la documentation interactive générée automatiquement par FastAPI :
[http://localhost:8000/docs](http://localhost:8000/docs)

ou au format Redoc :
[http://localhost:8000/redoc](http://localhost:8000/redoc)

### Accéder à l’interface Adminer

L’outil d’administration de la base de données est accessible à cette adresse :
[http://localhost:8080](http://localhost:8080)

Utilisez les paramètres suivants pour vous connecter :

| Champ           | Valeur           |
|-----------------|------------------|
| **Système**     | MySQL            |
| **Serveur**     | `db`             |
| **Utilisateur** | `${DB_USER}`     |
| **Mot de passe**| `${DB_PASSWORD}` |
| **Base**        | `${DB_NAME}`     |

Ces valeurs correspondent à celles définies dans votre fichier `.env`.
