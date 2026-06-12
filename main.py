from fastapi import FastAPI

app = FastAPI()

inventario_servidor = [
    {"id": 1, "nombre": "Poción de Vida", "cantidad": 3},
    {"id": 2, "nombre": "Escudo de Madera", "cantidad": 1},
    {"id": 3, "nombre": "Espada Oxidada", "cantidad": 1}
]
from fastapi import FastAPI
import sqlite3

app = FastAPI()

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



@app.get("/agregar")
def agregar_objeto():
    conexion = conectar_db()
    cursor = conexion.cursor()
    
    nuevo_nombre = "Escudo de Madera"
    nueva_cantidad = 1
    

    cursor.execute(
        "INSERT INTO items (nombre, cantidad) VALUES (?, ?)", 
        (nuevo_nombre, nueva_cantidad)
    )
    
  
    conexion.commit()
    conexion.close()
    
    return {"mensaje": f"¡{nuevo_nombre} guardado permanentemente en la Base de Datos! 💾"}