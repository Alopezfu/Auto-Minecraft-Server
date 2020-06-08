import urllib.request, os, sys, subprocess
from os import path

url = 'http://checkip.amazonaws.com/'
aws = urllib.request.urlopen(url)
ip=str(aws.read().decode('utf-8')).strip()
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
    config()

def menu():
    print("IP DEL SERVIDOR: " + ip) 
    print(" 1. Iniciar servidor")
    print(" 2. Configurar servidor")
    opt = int(input("Selecciona una opción: "))
    return opt

def config():
    os.chdir(dir)
    print('\x1bc')
    gamemode = input("Modo de juego (survival,creative,adventure,spectator): ")
    allownether = input("Permitir nether (true/false):")
    enablecommandblock = input("Permitir bloque de comandos (true/false):")
    oppermissionlevel = input("Nivel de permisos (1,2,3 o 4):")
    rconpassword = input("Contraseña (en blanco, sin constraseña):")
    motd = input("Nombre del servidor (en blanco, A Minecraft Server):")
    hardcore = input("Hablitar hardcore (true/false):")
    whitelist = input("Hablitar lista blanca (true/false):")
    pvp = input("Hablitar pvp (true/false):")
    difficulty = input("Dificultad (peaceful,easy,normal,hard):")
    spawnmonsters = input("Spawn de monstruos (true/false):")
    maxplayers = input("Jugadores permitidos (2,4,6 ...):")
    onlinemode = input("Solo jugadores premium (true/false):")
    spawnnpcs = input("Spawn de aldeanos (true/false):")

    print("Descargando ficheros...")
    url = 'https://raw.githubusercontent.com/Alopezfu/Auto-Minecraft-Server/master/template.txt'
    urllib.request.urlretrieve(url, dir + '/server.properties')

    f = open("server.properties", "a")
    f.write("gamemode=" + gamemode + '\n')
    f.write("allow-nether=true=" + allownether + '\n')
    f.write("enable-command-block=" + enablecommandblock + '\n')
    f.write("op-permission-level=" + oppermissionlevel + '\n')
    f.write("rcon.password=" + rconpassword + '\n')
    f.write("motd=" + motd + '\n')
    f.write("hardcore=" + hardcore + '\n')
    f.write("white-list=" + whitelist + '\n')
    f.write("pvp=" + pvp + '\n')
    f.write("difficulty=" + difficulty + '\n')
    f.write("spawn-monsters=" + spawnmonsters + '\n')
    f.write("max-players=" + maxplayers + '\n')
    f.write("online-mode=" + onlinemode + '\n')
    f.write("spawn-npcs=" + spawnnpcs)
    f.close()
    print('\x1bc')
    print("Server configurado")
    main()

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