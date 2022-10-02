from flask import Flask, jsonify, request
from joblib import load

model,vect = load('model_vect.joblib') 
app = Flask('Nombre')

@app.route('/',methods=['POST'])
def predict():
    # obtengo los datos del request post
    data = request.get_json(force=True)
    texto=data['texto']
    #el transform espera lista, aunque sea una sola string
    resp=model.predict(vect.transform([texto]))
    #no se puede pasar a json un array, pasar a lista
    return jsonify(resp.tolist())

app.run(host='127.0.0.1', port=5001)