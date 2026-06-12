import sqlite3

def inicializar_db():

    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()
    

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            cantidad INTEGER NOT NULL
        )
    """)
    
    conexion.commit()
    conexion.close()
    print("🔋 ¡Base de datos inicializada y lista!")

if __name__ == "__main__":
    inicializar_db()