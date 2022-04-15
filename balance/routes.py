from balance import app
from flask import render_template,jsonify,request
import sqlite3
from balance.modelos import ProcesaDatos


ruta_db = app.config['RUTA_BBDD']
data_manager = ProcesaDatos(ruta_db)



@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/api/v01/todos")
def todos():
    datos = data_manager.recupera_datos()
    return jsonify(datos)  