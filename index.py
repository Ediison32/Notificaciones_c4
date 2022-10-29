


from flask import Flask, request
import json
from twilio.rest import Client
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import mail  # correo electronico 


# Creamos un objeto flask

ap = Flask(__name__)

# cargamos la informacion de nuestro archivo config.json

info = open("config.json", "r") # asigno a info lo que esta en la carpeta "config.json ", la "r" es de read = leer 
send= json.loads(info.read())  # loads es el que nos permite entrar a la informacion 


'''
@app.route('/', methods=['GET'])
def test():
    return "no mames si dio "
'''
@ap.route('/send_sms', methods=['POST'])  # usar post cuando se van hacer consultas mas que todo 
def send_sms():
    try:
        
        account_sid = send['TWILIO_ACCOUNT_SID']
        auth_token =  send['TWILIO_AUTH_TOKEN']
        origen =      send['TWILIO_PHONE_NUMBER']
        client = Client(account_sid, auth_token)
        data = request.json
        contenido = data["contenido"]
        destino= data["destino"]

        message = client.messages.create(
            body = contenido,
            from_=origen,
            to = "+57"+destino
            )
        print (message)
        return"send success =  enviado" 
    except Exception as a:

        print(a)
        return "error"




if __name__ == '__main__':
    ap.run()
