from flask import Flask
app = Flask('test')
@app.route('/')
def index():
   return 'Hola mundo!'
app.run(debug=True, port=8888)