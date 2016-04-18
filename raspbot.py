# -*- coding: utf-8 -*-
 
import telebot # Librería de la API del bot.
from telebot import types # Tipos para la API del bot.
import time # Librería para hacer que el programa que controla el bot no se acabe.
import random
import urllib2
import datetime
import token
import os
import commands
import sched
TOKEN = '' #Nuestro token del bot
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
    bot.send_message( cid, "Comandos Disponibles: /help, /ping, /nmap,  /date, /temp, /saludo, /espacio")

@bot.message_handler(commands=['temp'])
def command_temp(m):
	cid = m.chat.id
	#temp = os.system('sudo /opt/vc/bin/vcgencmd measure_temp')
	temp = commands.getoutput('sudo /opt/vc/bin/vcgencmd measure_temp')	
	bot.send_message(cid, temp)

@bot.message_handler(commands=['camara'])
def command_camara(m):
	cid = m.chat.id
	camara = commands.getoutput('bash /home/pi/camara.sh')
	#img = urllib2.urlopen('home/pi/camara/shot').read()
	bot.send_message(cid,camara)
	photo = open('/home/pi/camara/shot')
	bot.send_photo(cid,img)
	commands.getouput('rm /home/pi/camara/shot')
		

@bot.message_handler(commands=['speedtest'])
def command_speedtest(m):
	cid = m.chat.id
	speedtest = commands.getoutput('speedtest-cli')
	bot.send_message(cid, speedtest)

@bot.message_handler(commands=['ping'])
def command_ping(m):
	cid = m.chat.id
	ping = commands.getoutput('sudo ping -c 4 8.8.8.8')
	bot.send_message(cid,ping)
	bot.send_message(cid,cid)  

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
@bot.message_handler(commands=['nmap'])
def command_nmap(m):
	cid = m.chat.id
	msg = "Este va a tardar"
	bot.send_message(cid, msg)
	info = commands.getoutput('sudo nmap -O -F 192.168.1.1/24')
	bot.send_message(cid,info)
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
