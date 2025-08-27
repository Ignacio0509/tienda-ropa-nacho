from flask import render_template, request, redirect, url_for
import requests
import json

PRENDAS_URL = "http://127.0.0.1:5000/api/prendas"
MARCAS_URL = "http://127.0.0.1:5000/api/marcas"

def get_prendas():
    """Maneja la página de listado y creación de prendas."""
    response_marcas = requests.get(MARCAS_URL)
    marcas_disponibles = response_marcas.json()
    
    if request.method == "POST":
        # Lógica para crear una nueva prenda a través de la API
        prenda_data = {
            "nombrePrenda": request.form["nombrePrenda"],
            "marcaId": request.form["marcaId"],
            "talla": request.form["talla"],
            "Color": request.form["Color"],
            "precio": request.form["precio"],
            "stock": request.form["stock"],
            "categoriaId": request.form["categoriaId"]
        }
        requests.post(PRENDAS_URL, json=prenda_data)
        return redirect(url_for("prendas"))

    # Lógica para mostrar todas las prendas desde la API
    response_prendas = requests.get(PRENDAS_URL)
    prendas = response_prendas.json()
    
    # Mapeo de IDs de marca a nombres de marca
    marcas_dict = {marca['_id']: marca['nombreMarca'] for marca in marcas_disponibles}
    for prenda in prendas:
        prenda['nombreMarca'] = marcas_dict.get(prenda['marcaId'], 'Marca no encontrada')
        
    return render_template("prendas_list.html", prendas=prendas, marcas_disponibles=marcas_disponibles)

def delete_prenda(item_id):
    """Maneja la eliminación de una prenda a través de la API."""
    requests.delete(f"{PRENDAS_URL}/{item_id}")
    return redirect(url_for("prendas"))

def edit_prenda(item_id):
    """Maneja la edición de una prenda."""
    response_prenda = requests.get(f"{PRENDAS_URL}/{item_id}")
    prenda = response_prenda.json()
    
    response_marcas = requests.get(MARCAS_URL)
    marcas_disponibles = response_marcas.json()

    if request.method == "POST":
        # Lógica para actualizar la prenda a través de la API
        prenda_data = {
            "nombrePrenda": request.form["nombrePrenda"],
            "marcaId": request.form["marcaId"],
            "talla": request.form["talla"],
            "Color": request.form["Color"],
            "precio": request.form["precio"],
            "stock": request.form["stock"],
            "categoriaId": request.form["categoriaId"]
        }
        requests.put(f"{PRENDAS_URL}/{item_id}", json=prenda_data)
        return redirect(url_for("prendas"))

    return render_template("prendas_form.html", prenda=prenda, marcas_disponibles=marcas_disponibles, title="Editar Prenda")