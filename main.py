import serial
import urllib2
__author__ = 'Guardiao Cloud'


apiKey = "xxxxxxxx-yyyy-zzzz-wwww-kkkkkkkkkkkk" #@todo Alterar Numero da API Key
serialKey = "GUC0001" #@todo Alterar numero de serie do dispositivo de Coleta
serialPort = '/dev/ttyS0' #@todo Alterar caminho da porta Serial do Arduino

if __name__ == '__main__':
    ser = serial.Serial(serialPort, 9600)
    while True:
        arduinoRead = ser.readline()
        arduinoRead = arduinoRead.replace('\n','').replace('\r','')
        listaVal = arduinoRead.split("|")
        param = "apiKey={0}&humidade={1}&temperatura={2}".format(apiKey,listaVal[0],listaVal[1])
        url = "http://guardiao.cl/collect/{0}/?{1}".format(serialKey,param)
        print urllib2.urlopen(url).read()
