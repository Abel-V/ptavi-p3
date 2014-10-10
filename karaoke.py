#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import sys
from smallsmilhandler import SmallSMILHandler


listarg = sys.argv
parser = make_parser()
Handler = SmallSMILHandler()
parser.setContentHandler(Handler)
try:
	parser.parse(open(listarg[1]))
except:
	sys.exit('Usage: python karaoke.py file.smil')  # y despues se para la ej.
List = Handler.get_tags()
for Dicc in List:
	print Dicc['etiqueta'], '\t',  # Con la coma al final no cambia de linea
	for Atrib in Dicc:
		if Atrib != 'etiqueta' and Dicc[Atrib] != "":
			print  Atrib, '=', Dicc[Atrib], '\t',
	print  # escribe una linea en blanco

