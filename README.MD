# INSTAGRAM

## **Tech**

> ### Python 3 

> ### PostgreSQL

> ### FastAPI

> ### Alembic

> ### .trunk

> ### Pydentic

> ### Pytest

> ### OAuth2 with Password (and hashing), Bearer with JWT tokens


***

## **Create file .env and past there:**
> export POSTGRES_URL=postgres

>export POSTGRES_USER=admin

>export POSTGRES_PASSWORD='mySUperP@swword'

>export POSTGRES_DB=instagram_db


## **Run application with docker-compose**
***
### **Install [Docker]((https://docs.docker.com/engine/install/ubuntu/)) and after run code in terminal**
***
### **1. Clone application from GitHub:**
```bash
git clone https://github.com/evgcroxsoft/Instagram.git
```
### **2. Go to downloaded repository**

### **3. Build application with command:**
```bash
sudo docker-compose build
```
### **4. Start application:**
```bash
sudo docker-compose up
```
## **Open link**

http://127.0.0.1:8000/docs#/


## **Stop application with docker-compose**
```bash
sudo docker-compose down
```