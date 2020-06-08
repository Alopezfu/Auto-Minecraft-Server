import urllib.request, os, sys, subprocess
from os import path

url = 'http://checkip.amazonaws.com/'
f = urllib.request.urlopen(url)
ip=str(f.read().decode('utf-8')).strip()
dir = os.path.expanduser('~') + '/minecraft-server'

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

def config():
    print('\x1bc')
    gamemode = input("Modo de juego (survival,creative,adventure,spectator): ")
    allownether = input("Permitir nether (true/false):")
    enablecommandblock = input("Permitir bloque de comandos (true/false):")
    oppermissionlevel = int(input("Nivel de permisos (1,2,3 o 4):"))
    rconpassword = input("Contraseña (en blanco, sin constraseña):")
    motd = input("Nombre del servidor (en blanco, A Minecraft Server):")
    hardcore = input("Hablitar hardcore (true/false):")
    whitelist = input("Hablitar lista blanca (true/false):")
    pvp = input("Hablitar pvp (true/false):")
    difficulty = input("Dificultad (peaceful,easy,normal,hard):")
    spawnmonsters = input("Spawn de monstruos (true/false):")
    maxplayers = int(input("Jugadores permitidos (2,4,6 ...):"))
    onlinemode = input("Solo jugadores premium (true/false):")
    spawnnpcs = input("Spawn de aldeanos (true/false)")

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
            config()
        else:
            main()

main()