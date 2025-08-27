from flask import render_template, request, redirect, url_for, jsonify
import requests
import json

BASE_URL = "http://127.0.0.1:5000/api/marcas"

def get_marcas():
    """Maneja la página de listado y creación de marcas."""
    if request.method == "POST":
        # Lógica para crear una nueva marca a través de la API
        data = {"nombreMarca": request.form["nombreMarca"]}
        requests.post(BASE_URL, json=data)
        return redirect(url_for("marcas"))
    
    # Lógica para mostrar todas las marcas desde la API
    response = requests.get(BASE_URL)
    marcas = response.json()
    return render_template("marcas_list.html", marcas=marcas)

def delete_marca(item_id):
    """Maneja la eliminación de una marca a través de la API."""
    requests.delete(f"{BASE_URL}/{item_id}")
    return redirect(url_for("marcas"))

def edit_marca(item_id):
    """Maneja la edición de una marca."""
    response = requests.get(f"{BASE_URL}/{item_id}")
    marca = response.json()
    
    if request.method == "POST":
        # Lógica para actualizar la marca a través de la API
        data = {"nombreMarca": request.form["nombreMarca"]}
        requests.put(f"{BASE_URL}/{item_id}", json=data)
        return redirect(url_for("marcas"))
    
    # Muestra el formulario de edición
    return render_template("marcas_form.html", marca=marca, title="Editar Marca")