
#from crypt import methods
from email import message
from urllib import response
from flask import Flask, request
import json
#from pyparsing import html_comment
from twilio.rest import Client
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail  # correo electronico 


# Creamos un objeto flask

ap = Flask(__name__)

# cargamos la informacion de nuestro archivo config.json

info = open("config.json", "r") # asigno a info lo que esta en la carpeta "config.json ", la "r" es de read = leer 
send= json.loads(info.read())  # loads es el que nos permite entrar a la informacion 


'''
@ap.route('/', methods=['GET'])
def test():
    return "no mames si dio "
'''

# envio de mensajes por numero de celular usando  twilio
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

        print("El error esa ",a)
        return "error"

#envio de mensajes por email 
@ap.route('/send_email', methods=['POST'])
def send_email():
    data= request.json  # recibe un json 
    contenido= data["contenido"] # asigno un trozo del json 
    destino= data["destino"]  # destino 
    asunto= data["asunto"]                   # asunto 
    print(contenido,destino,asunto)
    message = Mail(
        from_email= send['SENDGRID_FROM_EMAIL'],
        to_emails = destino,
        subject= asunto,
        html_content=contenido
        )

    try:
        sengrid= SendGridAPIClient(send['SENDGRID_API_KEY'])
        response= sengrid.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
        return "send succes, funciona"
    except Exception as a:
        print(a)
        return "error"


if __name__ == '__main__':
    ap.run()
