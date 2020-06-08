import urllib.request, os, sys, subprocess
from os import path

dir = os.path.expanduser('~') + '/minecraft-server'
ip = "8.8.8.8"

def getJAR():
    os.mkdir(dir)
    print("Descargando ficheros...")
    url = 'https://launcher.mojang.com/v1/objects/bb2b6b1aefcd70dfd1892149ac3a215f6c636b07/server.jar'
    urllib.request.urlretrieve(url, dir + '/server.jar')

def install():
    os.chdir(dir)
    subprocess.run(["java", "-jar", "server.jar", "nogui"])
    s = open("eula.txt").read()
    s = s.replace('false', 'true')
    f = open("eula.txt", 'w')
    f.write(s)
    f.close()
    print('\x1bc')
    main()

def menu():
    print("IP DEL SERVIDOR: " + ip) 
    print(" 1. Iniciar servidor")
    print(" 2. Configurar servidor")
    opt = int(input("Selecciona una opción: "))
    return opt

def main():
    print('\x1bc')
    if not path.exists(dir + "/eula.txt"):
        getJAR()
        install()
    else:
        os.chdir(dir)
        opt = menu()
        if opt == 1:
            subprocess.run(["java", "-jar", dir + "/server.jar", "nogui"])
        elif opt == 2:
            name =  input("Nombre del server: ")
            players =  int(input("Numero maxsimo de jugadores: "))
            mode =  input("Modo de juego (survival/creative): ")
            commandBlock = input("Permitir command-block (si/no):")
            pvp = input("Permitir pvp (si/no):")
        else:
            main()

main()