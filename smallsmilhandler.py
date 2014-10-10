#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class SmallSMILHandler(ContentHandler):

    def __init__(self):
        #Diccionario de Listas con todo lo que puedo tener (sólamente para
        #buscar los nombres, no para guardar valores)
        self.KaraokeDicc = {
            'root-layout': ['width', 'height', 'background-color'],
            'region': ['id', 'top', 'bottom', 'left', 'right'],
            'img': ['src', 'region', 'begin', 'dur'],
            'audio': ['src', 'begin', 'dur'],
            'textstream': ['src', 'region']
        }
        #Lista donde guardaré las etiquetas que encuentre; serán diccionarios
        #cada una de ellas
        self.Etiquetas = []

    def startElement(self, name, attrs):
        if name in self.KaraokeDicc:
            Atributos = {}  # creo el diccionario para guardar valores
            Atributos['etiqueta'] = name  # Guardo el nombre de la etiqueta
                                          # como una entrada del diccionario
            for Atributo in self.KaraokeDicc[name]:  # busco en la entrada=name
                Atributos[Atributo] = attrs.get(Atributo, "")
                #Esta funcion guarda el valor de Atributo, si existe en esa
                #etiqueta, y si no, guarda un string vacío
            self.Etiquetas.append(Atributos)

    def get_tags(self):
        return self.Etiquetas


if __name__ == "__main__":

    parser = make_parser()
    Handler = SmallSMILHandler()
    parser.setContentHandler(Handler)
    parser.parse(open('karaoke.smil'))
    print Handler.get_tags()
