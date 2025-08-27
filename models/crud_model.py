from bson.objectid import ObjectId

class CrudModel:
    """Clase para gestionar las operaciones CRUD en las colecciones de MongoDB."""

    def __init__(self, collection):
        """Inicializa el modelo con la colección de la base de datos."""
        self.collection = collection

    def get_all(self):
        """Recupera todos los documentos de la colección."""
        return list(self.collection.find())

    def get_by_id(self, item_id):
        """Recupera un documento por su ID."""
        try:
            return self.collection.find_one({"_id": ObjectId(item_id)})
        except Exception:
            return None

    def create(self, item_data):
        """Crea un nuevo documento en la colección."""
        return self.collection.insert_one(item_data).inserted_id

    def update(self, item_id, item_data):
        """Actualiza un documento existente por su ID."""
        return self.collection.update_one({"_id": ObjectId(item_id)}, {"$set": item_data})

    def delete(self, item_id):
        """Elimina un documento por su ID."""
        return self.collection.delete_one({"_id": ObjectId(item_id)})