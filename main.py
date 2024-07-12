from flask import Flask
import random

app = Flask(__name__)

facts_list = {'La mayoría de las personas que sufren adicción tecnológica experimentan un fuerte estrés cuando se encuentran fuera del área de cobertura de la red o no pueden utilizar sus dispositivos','Según un estudio de 2019, más del 60% de las personas responden a mensajes de trabajo en sus smartphones en los 15 minutos siguientes a salir del trabajo','Las redes sociales tienen aspectos positivos y negativos, y debemos ser conscientes de ambos cuando utilicemos estas plataformas','Elon Musk afirma que las redes sociales están diseñadas para mantenernos dentro de la plataforma, para que pasemos el mayor tiempo posible viendo contenidos'}
side = {'Cara','Sello'}

@app.route("/")
def menu():
    return '<a href="/random_fact">¡Ver un dato aleatorio!</a>''<a href="/car">¡Mira un Auto!</a>''<a href="/historia">¡Lee un pequeño cuento!</a>''<a href="/coin">¡Vamos a lanzar una moneda!</a>'

@app.route('/car')
def car():
    return '<h1> Mira un auto</h1>''<p>😎🚗</p>'

@app.route('/historia')
def cuento():
    return '<h1>Una Pequeña Historia</h1>''<p>Hace mucho mucho tiempo, un niño paseaba por un prado en cuyo centro encontró un árbol con un cartel que decía: soy un árbol encantado, si dices las palabras mágicas, lo verás. El niño trató de acertar el hechizo, y probó con abracadabra, supercalifragilisticoespialidoso, tan-ta-ta-chán, y muchas otras, pero nada. Rendido, se tiró suplicante, diciendo: "¡¡por favor, arbolito!!", y entonces, se abrió una gran puerta en el árbol. Todo estaba oscuro, menos un cartel que decía: "sigue haciendo magia". Entonces el niño dijo "¡¡Gracias, arbolito!!", y se encendió dentro del árbol una luz que alumbraba un camino hacia una gran montaña de juguetes y chocolate. El niño pudo llevar a todos sus amigos a aquel árbol y tener la mejor fiesta del mundo, y por eso se dice siempre que "por favor" y "gracias", son las palabras mágicas</p>'

@app.route("/random_fact")
def random_factou():
    return f'<p>{random.choice(list(facts_list))}</p>'

@app.route('/secret')
def secret():
    return '<h1>¡¡VAYA!!</h1>''<p>Eres bastante curioso encontraste una pagina web secreta mira un diamante</p>''<h2>💎</h2>'

@app.route('/coin')
def coin():
    return f'<p>tiraste una moneda esto cayo:{random.choice(list(side))}</p>'

app.run(debug=True)
