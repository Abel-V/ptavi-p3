from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import sys
from smallsmilhandler import SmallSMILHandler
import os


class KaraokeLocal:

    def __init__(self, fichero):
        parser = make_parser()
        Handler = SmallSMILHandler()
        parser.setContentHandler(Handler)
        parser.parse(open(fichero))
        self.List = Handler.get_tags()

    def __str__(self):
        Str = ""
        for Dicc in self.List:
            Str = Str + Dicc['etiqueta'] + '\t'
            for Atrib in Dicc:
                if Atrib != 'etiqueta' and Dicc[Atrib] != "":
                    Str = Str + Atrib + ' = "' + Dicc[Atrib] + '"\t'
            Str = Str + '\n'
        return Str

    def do_local(self):
        for Dicc in self.List:
            print Dicc['etiqueta'], '\t',
            for Atrib in Dicc:
                if Atrib != 'etiqueta' and Dicc[Atrib] != "":
                    if Atrib == 'src':
                        recurso = Dicc[Atrib]
                        os.system("wget -q " + recurso)
                        NombreLocal = recurso.split('/')[-1]  # Ult. elemento
                        Dicc[Atrib] = NombreLocal  # (nombre de lo descargado)
                    print Atrib, '= "' + Dicc[Atrib] + '" \t',
            print


if __name__ == "__main__":

    listarg = sys.argv
    try:
        Khandler = KaraokeLocal(listarg[1])
    except:
        sys.exit('Usage: python karaoke.py file.smil')  # y despues para la ej.
    print Khandler.__str__()
    Khandler.do_local()
