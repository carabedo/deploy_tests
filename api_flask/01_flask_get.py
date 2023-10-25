##01_flask_get.py
from flask import Flask, jsonify, request

#instancio una app, le paso el nombre (no se usa para nada)
app = Flask('API Get') #nombre de la app

#ahora voy a crear la funcion principal de la app
#para esto le agrego un decorador a una funcion comun
#un decorador solo es una @ antes de la definicion de la funcion:



incomes = [
    { 'description': 'salary', 'amount': 5000 }
]



@app.route('/')
def funcionprincipal():
    # no importa el nombre el decorador se encarga de definir
    # que esta funcion se va a ejecutar cuando
    # hagamos un requests GET a '/'
    # obtengo los datos del request que viene de la peticion externa 
    return jsonify(incomes)
app.run(host='127.0.0.1',  port=8888 )

# host local puerto el que quieras