from sqlalchemy import create_engine

# URL de la base de datos
DATABASE_URL = "postgresql://postgres:1234@localhost:5432/web"

# Crear un motor de conexión
engine = create_engine(DATABASE_URL)

def check_connection():
    try:
        # Intentar conectar a la base de datos
        with engine.connect() as connection:
            print("Conexión exitosa a la base de datos.")
    except Exception as e:
        print(f"No se pudo conectar a la base de datos: {e}")

if __name__ == "__main__":
    check_connection()

