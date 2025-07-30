#marcas asociadas al compass
from flask import Blueprint, request, jsonify
from app.models.marcas import Marcas

marcas_endpoints = Blueprint('marcas_endpoints', __name__)
 
# GET todos los libros sin parametros y con id.
# Ejemplo de endpoint:
# http://127.0.0.1:5000/libreria/api/v1/libros?id=6823e02cea9cb5e5156c4bd3
# http://127.0.0.1:5000/libreria/api/v1/libros

@marcas_endpoints.route('/marcas', methods=['GET'])
def obtenerMarcass():
    idMarca = request.args.get('id')

    if idMarca:
        marcas = marcas.obtener_por_id(idMarca)
        if marcas:
            return jsonify(Marca), 200
        return jsonify({"error": "Marca no encontrada"}), 404

    libros = LibroModel.obtener_todos()
    return jsonify(libros), 200
