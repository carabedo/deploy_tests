from flask import Flask
app = Flask('primersitio')

@app.route('/')
def index():
   return 'Hola mundo!'





@app.route('/about/')
def about():
   return 'Soy fernando!'



@app.route('/html/')
def html():
   return '<h1>Hola, en negritas!</h1>'





@app.route('/html/js/')
def htmljs():
   return '''<body>

    <h1> Ejemplo de pagina en HTML con Javascript</h1>

    <h2> Ingrese el nombre de un articulo que desee conocer su precio.</h2>
    
    <form action="">
      <label for="query">Busqueda: </label>
      <input type="text" name="query" class='q' id="q">

    </form>

    <button onclick="getItems()">Buscar</button>

    <ul>
    </ul>
<script>

function getItems(){    
var requestOptions = {
  method: 'GET',
  redirect: 'follow'
};

try {
  let q = document.querySelector("input.q")
    let url = "https://7pyngmccwa.execute-api.us-east-1.amazonaws.com/default/apitest?q="+q.value
  
  document.querySelector('ul').innerHTML=''
  fetch(url, requestOptions)
  .then(response => response.json())
  .then(result => renderlist(result))
  .catch(error => console.log('error', error));
    
} catch (error) {
  
 alert(error)

}
}

function renderlist(arrayItems){
for (x of arrayItems) {
    console.log(x)
    document.querySelector('ul').innerHTML += '<li>' + x.name +' <br> precio: ' + x.price + '$ </li>';
}

}

</script>    
</body>
<style>
    body {
        width: 70%;
        margin: 100px auto;
        background-color: bisque;
    }

    h2 {
    color: rgb(249, 41, 27);
    }
</style>'''

app.run(debug=True, port=8000)