##02_flask_post.py
from flask import Flask, jsonify, request
import numpy as np

app = Flask('server post')
@app.route('/',methods=['POST']) #aca definimos q recibe requests POST
def predict(): #la funcion q se ejecuta 
    data = request.get_json(force=True)
    try:
        a_vector = np.array(data['a']).astype('int')
        # Le damos forma de un diccionario para poder hacer el traspaso a json trivialmente
        a_2=a_vector**2    
        resp={'response' : a_2.tolist() }#importante pasar a lista los numpy arrays 

    except:
        resp={'response' : 'no esta presente la variable aaaaaa'}
        # en esta linea, transformamos el diccionario en json con jsonify (funcionalidad de flask)
        # este json es incorporado en el cuerpo de la respuesta
    return jsonify(resp)
app.run(host='127.0.0.1', port=6000)