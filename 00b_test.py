from flask import Flask
app = Flask('primersitio')

@app.route('/')
def index():
   return 'Hola mundo!'

app.run(debug=True, port=8000)