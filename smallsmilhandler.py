#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler

class SmallSMILHandler(ContentHandler):

    def __init__ (self):

    root-layout (width, height, background-color):

    region (id, top, bottom, left, right):

    img (src, region, begin, dur):

    audio (src, begin, dur):

    textstream (src, region):

    def get tags():


#1o cogí de Github la carpeta ptavi-p3 con: git clone "http del repo ptavi-p3"
#añadirlo 1a vez: hacer git add fichero
#luego se actualiza en el repo local con: git commit -m "mensaje explicativo"
#y finalmente en el github con git push
