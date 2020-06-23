#Importacao da biblioteca para controle GPIO
import RPi.GPIO as GPIO

#Importacao das bibliotecas para requisicoes HTTP
import urllib
import urllib2

#Importacao da biblioteca para delay
import time

#Configuracao do GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#Declaracao dos pinos dos dispositivos
button = 17
led = 26

#Configuracao de entrada e saida dos dispositivos
GPIO.setup(button, GPIO.IN)
GPIO.setup(led, GPIO.OUT)

#Super loop
while True:
    
    #Verificando o estado do botao
    if GPIO.input(button) == GPIO.HIGH:

        #Realizando um POST no servidor com o estado do botao
        parametro = { 'EstadoBotao':'Botao Pressionado' }
        url = 'http://192.168.0.110/estadoBotao'
        dado = urllib.urlencode(parametro)
        requisicao = urllib2.Request(url, dado)
        resposta = urllib2.urlopen(requisicao).read()

    else:

        #Realizando um POST no servidor com o estado do botao
        parametro = { 'EstadoBotao':'Botao Nao Pressionado' }
        url = 'http://192.168.0.110/estadoBotao'
        dado = urllib.urlencode(parametro)
        requisicao = urllib2.Request(url, dado)
        resposta = urllib2.urlopen(requisicao).read()
    
    #Realizando um GET no servidor e guardando o resultado da requisicao
    url = 'http://192.168.0.110/estadoBotao'
    resposta = urllib.urlopen(url).read()

    #Verificando o resultado da requisicao GET
    if resposta == "Botao Pressionado":

        #Acionando o led
        GPIO.output(led, GPIO.HIGH)

    elif resposta == "Botao Nao Pressionado": 

        #Apagando o led
        GPIO.output(led, GPIO.LOW)
    
    #Pequeno atraso para a proxima leitura
    time.sleep(0.3) 