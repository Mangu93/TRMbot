# -*- coding: utf-8 -*-
 
import telebot # Librería de la API del bot.
from telebot import types # Tipos para la API del bot.
import time # Librería para hacer que el programa que controla el bot no se acabe.
import random
import datetime
import token
import os
import commands
import sched
TOKEN = 'Enter your token' #Nuestro token del bot
s = sched.scheduler(time.time, time.sleep)
bot = telebot.TeleBot(TOKEN) # Creamos el objeto de nuestro bot.
#############################################
#Listener
def listener(messages): # Con esto, estamos definiendo una función llamada 'listener', que recibe como parámetro un dato llamado 'messages'.
    for m in messages: # Por cada dato 'm' en el dato 'messages'
        cid = m.chat.id # Almacenaremos el ID de la conversación.
        if m.content_type == 'text':
            print "[" + str(cid) + "]: " + m.text # Y haremos que imprima algo parecido a esto -> [52033876]: /start
 
bot.set_update_listener(listener) # Así, le decimos al bot que utilice como función escuchadora nuestra función 'listener' declarada arriba.
#############################################
#Funciones
@bot.message_handler(commands=['help']) 
def command_ayuda(m): 
    cid = m.chat.id 
    bot.send_message( cid, "Comandos Disponibles: /help, /date, /temp, /saludo, /espacio")

@bot.message_handler(commands=['temp'])
def command_temp(m):
	cid = m.chat.id
	#temp = os.system('sudo /opt/vc/bin/vcgencmd measure_temp')
	temp = commands.getoutput('sudo /opt/vc/bin/vcgencmd measure_temp')	
	bot.send_message(cid, temp)

@bot.message_handler(commands=['date'])
def command_temp(m):
        cid = m.chat.id
	saludo = commands.getoutput('date')
        bot.send_message(cid, saludo)
@bot.message_handler(commands=['saludo'])
def command_temp(m):
        cid = m.chat.id
	saludo = commands.getoutput('bash /home/pi/saludo.sh')
        bot.send_message(cid, saludo)

@bot.message_handler(commands=['espacio'])
def command_espacio(m):
        cid = m.chat.id
        info = commands.getoutput('df -h')
        bot.send_message(cid, info)
""" 
def timer(sc,m):
	cid = m.chat.id
	info = commands.getoutput('sudo ping www.google.es')
	if "unreachable" not in info:
		bot.send(cid,info)
	else:
		msg = 'There is some trouble with the network'
		bot.send(cid,info)
	
""" 
#############################################
#Peticiones
bot.polling(none_stop=True) # Con esto, le decimos al bot que siga funcionando incluso si encuentra algun fallo.
