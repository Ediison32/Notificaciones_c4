
# creamos sitio web con python 

from flask import Flask,request

# cramos  obeto Flassk

app = Flask(__name__)


# creamos servicion web 

@app.route('/', methods=['GET'])
def test():
    return "no mames si dio "


@app.route('/hola/<string:name>', methods=['GET'])
def hola(name: str):
    return " hola perro bien nnn " + name


# ejecutamos programa 

if __name__ == '__main__':
    app.run()