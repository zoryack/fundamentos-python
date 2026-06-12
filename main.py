from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3

app = FastAPI()

class ItemEsquema(BaseModel):
    nombre: str
    cantidad: int

def conectar_db():
    conexion = sqlite3.connect("inventario.db")
    conexion.row_factory = sqlite3.Row
    return conexion

@app.get("/inventario")
def obtener_inventario():
    conexion = conectar_db()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM items")
    filas = cursor.fetchall()
    lista_items = [dict(fila) for fila in filas]
    conexion.close()
    return lista_items


@app.post("/items")
def agregar_objeto(item_nuevo: ItemEsquema):
    conexion = conectar_db()
    cursor = conexion.cursor()
    

    cursor.execute(
        "INSERT INTO items (nombre, cantidad) VALUES (?, ?)", 
        (item_nuevo.nombre, item_nuevo.cantidad)
    )
    
    conexion.commit()
    conexion.close()
    
    return {
        "mensaje": "¡Objeto guardado dinámicamente!",
        "datos_guardados": item_nuevo
    }