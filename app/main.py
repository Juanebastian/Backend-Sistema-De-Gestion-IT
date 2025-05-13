# main.py
from fastapi import FastAPI, HTTPException
import psycopg2
from pydantic import BaseModel

app = FastAPI()

# Modelo para los datos
class User(BaseModel):
    name: str
    email: str

# Función para conectarse a PostgreSQL
def get_connection():
    return psycopg2.connect(
        dbname="gestion_it",
        user="postgres",
        password="juan11",
        host="localhost",  # o la IP del servidor
        port="5432"
    )

@app.post("/users/")
def create_user(user: User):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = "INSERT INTO users (name, email) VALUES (%s, %s);"
        cursor.execute(query, (user.name, user.email))
        conn.commit()
        cursor.close()
        conn.close()
        return {"message": "Usuario creado exitosamente"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
