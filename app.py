from flask import Flask, render_template
from flask_restful import Api
import controllers.marcas_controller as marcas_ctrl
import controllers.prendas_controller as prendas_ctrl
from api.marcas_api import MarcasApi
from api.prendas_api import PrendasApi

app = Flask(__name__, template_folder='views/templates', static_folder='views/static')
api = Api(app)

# Rutas de la API
api.add_resource(MarcasApi, '/api/marcas', '/api/marcas/<string:item_id>')
api.add_resource(PrendasApi, '/api/prendas', '/api/prendas/<string:item_id>')

# Rutas para la Interfaz Web (Vistas)
@app.route("/")
def index():
    """Ruta de la página de inicio."""
    return render_template("index.html")

# Rutas para Marcas
@app.route("/marcas", methods=["GET", "POST"])
def marcas():
    """Ruta para ver y crear marcas."""
    return marcas_ctrl.get_marcas()

@app.route("/marcas/delete/<item_id>")
def delete_marca(item_id):
    """Ruta para eliminar una marca."""
    return marcas_ctrl.delete_marca(item_id)

@app.route("/marcas/edit/<item_id>", methods=["GET", "POST"])
def edit_marca(item_id):
    """Ruta para editar una marca."""
    return marcas_ctrl.edit_marca(item_id)

# Rutas para Prendas
@app.route("/prendas", methods=["GET", "POST"])
def prendas():
    """Ruta para ver y crear prendas."""
    return prendas_ctrl.get_prendas()

@app.route("/prendas/delete/<item_id>")
def delete_prenda(item_id):
    """Ruta para eliminar una prenda."""
    return prendas_ctrl.delete_prenda(item_id)

@app.route("/prendas/edit/<item_id>", methods=["GET", "POST"])
def edit_prenda(item_id):
    """Ruta para editar una prenda."""
    return prendas_ctrl.edit_prenda(item_id)

if __name__ == '__main__':
    app.run(debug=True)