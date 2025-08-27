import os
from pymongo import MongoClient
from dotenv import load_dotenv

# Carga las variables de entorno del archivo .env
load_dotenv()

# Obtiene la URI de MongoDB desde las variables de entorno
mongo_uri = os.getenv("MONGO_URI")
if not mongo_uri:
    raise ValueError("MONGO_URI no está configurada en el archivo .env")

# Conexión a la base de datos
try:
    client = MongoClient(mongo_uri)
    db = client.get_database("tiendaRopa")#
    marcas_collection = db.get_collection("Marcas")
    prendas_collection = db.get_collection("Prendas")
    print("Conexión a MongoDB exitosa.")
except Exception as e:
    print(f"Error al conectar a MongoDB: {e}")