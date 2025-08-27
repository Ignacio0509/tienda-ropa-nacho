from flask import jsonify, request
from flask_restful import Resource
from models.db_config import prendas_collection, marcas_collection
from models.crud_model import CrudModel
from bson.objectid import ObjectId

class PrendasApi(Resource):
    """API para las operaciones CRUD de la colección de Prendas."""
    
    def __init__(self):
        self.model = CrudModel(prendas_collection)
        self.marcas_model = CrudModel(marcas_collection)

    def get(self, item_id=None):
        """Obtiene una prenda específica o todas las prendas."""
        if item_id:
            prenda = self.model.get_by_id(item_id)
            if prenda:
                prenda['_id'] = str(prenda['_id'])
                if 'marcaId' in prenda:
                    prenda['marcaId'] = str(prenda['marcaId'])
                return jsonify(prenda)
            return {"message": "Prenda no encontrada"}, 404
        else:
            prendas = self.model.get_all()
            for prenda in prendas:
                prenda['_id'] = str(prenda['_id'])
                if 'marcaId' in prenda:
                    prenda['marcaId'] = str(prenda['marcaId'])
            return jsonify(prendas)

    def post(self):
        """Crea una nueva prenda."""
        data = request.get_json()
        # Validación básica de datos
        required_fields = ["nombrePrenda", "marcaId", "talla", "Color", "precio", "stock", "categoriaId"]
        if not all(field in data for field in required_fields):
            return {"message": f"Faltan campos requeridos: {required_fields}"}, 400
        
        # Validación de marcaId
        try:
            marca_id = ObjectId(data['marcaId'])
            if not self.marcas_model.get_by_id(data['marcaId']):
                return {"message": "La marcaId proporcionada no existe"}, 400
        except:
            return {"message": "La marcaId proporcionada no es un ID válido"}, 400
            
        new_id = self.model.create(data)
        return {"message": "Prenda creada", "id": str(new_id)}, 201

    def put(self, item_id):
        """Actualiza una prenda existente."""
        data = request.get_json()
        if not data:
            return {"message": "No hay datos para actualizar"}, 400
        
        # Si se intenta actualizar marcaId, validar que sea un ID válido
        if 'marcaId' in data:
            try:
                marca_id = ObjectId(data['marcaId'])
                if not self.marcas_model.get_by_id(data['marcaId']):
                    return {"message": "La marcaId proporcionada no existe"}, 400
            except:
                return {"message": "La marcaId proporcionada no es un ID válido"}, 400

        result = self.model.update(item_id, data)
        if result.modified_count > 0:
            return {"message": "Prenda actualizada"}, 200
        return {"message": "Prenda no encontrada"}, 404

    def delete(self, item_id):
        """Elimina una prenda."""
        result = self.model.delete(item_id)
        if result.deleted_count > 0:
            return {"message": "Prenda eliminada"}, 200
        return {"message": "Prenda no encontrada"}, 404