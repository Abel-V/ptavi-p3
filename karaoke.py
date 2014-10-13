#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import sys
from smallsmilhandler import SmallSMILHandler
import os


listarg = sys.argv
parser = make_parser()
Handler = SmallSMILHandler()
parser.setContentHandler(Handler)
try:
	parser.parse(open(listarg[1]))
except:
	sys.exit('Usage: python karaoke.py file.smil')  # y despues se para la ej.
List = Handler.get_tags()
#ListOriginal = Handler.get_tags()
for Dicc in List:
	print Dicc['etiqueta'], '\t',  # Con coma al final no cambia de linea
	for Atrib in Dicc:
		if Atrib != 'etiqueta' and Dicc[Atrib] != "":
			if Atrib == 'src':
				recurso = Dicc[Atrib]
				os.system("wget -q " + recurso)
				NombreLocal = recurso.split('/')[-1]  # Me quedo con lo último
				Dicc[Atrib] = NombreLocal  # Que es el nombre de lo descargado
			print  Atrib, '= "' + Dicc[Atrib] + '" \t',
			
	print  # escribe una linea en blanco

