from fastapi import FastAPI
import psycopg2
from psycopg2.extras import RealDictCursor
import os

app = FastAPI()

def get_db_connection():
    return psycopg2.connect(
        host=os.getenv('DB_HOST'),
        database=os.getenv('DB_NAME'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASS')
    )

@app.get("/farmacias")
def get_puntos():
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("SELECT nombre, descripcion, categoria, ST_X(geom) as lon, ST_Y(geom) as lat FROM puntos_interes")
    puntos = cur.fetchall()
    cur.close()
    conn.close()
    return puntos

@app.post("/registrar")
def registrar_punto(datos: dict):
    conn = get_db_connection()
    cur = conn.cursor()
    query = "INSERT INTO puntos_interes (nombre, descripcion, categoria, geom) VALUES (%s, %s, %s, ST_SetSRID(ST_Point(%s, %s), 4326))"
    cur.execute(query, (datos['nombre'], datos['descripcion'], datos['categoria'], datos['lon'], datos['lat']))
    conn.commit()
    cur.close()
    conn.close()
    return {"status": "ok"}
