##01_flask_get.py
from flask import Flask, request

#instancio una app, le paso el nombre (no se usa para nada)
app = Flask('Servidor Get') #nombre de la app

#ahora voy a crear la funcion principal de la app
#para esto le agrego un decorador a una funcion comun
#un decorador solo es una @ antes de la definicion de la funcion:

@app.route('/') #metodo http que va a usar
def funcionprincipal():
    # no importa el nombre el decorador se encarga de definir
    # que esta funcion se va a ejecutar cuando
    # hagamos un requests GET a '/'
    # obtengo los datos del request que viene de la peticion externa 
    data=request.args.to_dict() 
    # (el metodo to_dict lo transforma en un diccionario)
    try:# uso try por si no me envian una variable a           
        resp='el cuadrado de a es : '+str(int(data['a'])*int(data['a']))
    except:
        resp='no se envio la variable a'
    return(resp)
app.run(host='127.0.0.1',  port=5002 )

# host local puerto el que quieras