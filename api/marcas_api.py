from flask import jsonify, request
from flask_restful import Resource
from models.db_config import marcas_collection
from models.crud_model import CrudModel
from bson.objectid import ObjectId

class MarcasApi(Resource):
    """API para las operaciones CRUD de la colección de Marcas."""
    
    def __init__(self):
        self.model = CrudModel(marcas_collection)

    def get(self, item_id=None):
        """Obtiene una marca específica o todas las marcas."""
        if item_id:
            marca = self.model.get_by_id(item_id)
            if marca:
                marca['_id'] = str(marca['_id'])
                return jsonify(marca)
            return {"message": "Marca no encontrada"}, 404
        else:
            marcas = self.model.get_all()
            for marca in marcas:
                marca['_id'] = str(marca['_id'])
            return jsonify(marcas)

    def post(self):
        """Crea una nueva marca."""
        data = request.get_json()
        if not data or 'nombreMarca' not in data:
            return {"message": "El campo 'nombreMarca' es requerido"}, 400
        
        new_id = self.model.create({"nombreMarca": data['nombreMarca']})
        return {"message": "Marca creada", "id": str(new_id)}, 201

    def put(self, item_id):
        """Actualiza una marca existente."""
        data = request.get_json()
        if not data or 'nombreMarca' not in data:
            return {"message": "El campo 'nombreMarca' es requerido"}, 400
        
        result = self.model.update(item_id, {"nombreMarca": data['nombreMarca']})
        if result.modified_count > 0:
            return {"message": "Marca actualizada"}, 200
        return {"message": "Marca no encontrada"}, 404

    def delete(self, item_id):
        """Elimina una marca."""
        result = self.model.delete(item_id)
        if result.deleted_count > 0:
            return {"message": "Marca eliminada"}, 200
        return {"message": "Marca no encontrada"}, 404