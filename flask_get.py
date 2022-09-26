from flask import Flask, jsonify, request
app = Flask('Servidor Get') #nombre de la app
@app.route('/',methods=['GET']) #metodo http que va a usar
def funcionprincipal():#no importa el nombre el decorador se encarga
    # obtengo los datos del request que viene de la peticion externa 
    data=request.args.to_dict() # (el metodo to_dict lo transforma en un diccionario)
    try:# uso try por si no me envian una variable a           
        resp='el cuadrado de a es : '+str(int(data['a'])*int(data['a']))
    except:
        resp='no se envio la variable a'
    return(resp)
app.run(port=8000,host='0.0.0.0' )# host local puerto el que quieras