#Produzido por Kaian Vinicius, @Kaian32
pronto = 'false'
import sys #importa comandos do sistema
from os import system #importa sistema
import time #importa mecanismos de tempo
system('cls') #limpa o que tinha antes

#animação de loading
def loading():
    while pronto == 'false':
        sys.stdout.write('\rCarregando o CopaManager! |')
        time.sleep(0.1)
        sys.stdout.write('\rCarregando o CopaManager! /')
        time.sleep(0.1)
        sys.stdout.write('\rCarregando o CopaManager! -')
        time.sleep(0.1)
        sys.stdout.write('\rCarregando o CopaManager! \\')
        time.sleep(0.1)
    sys.stdout.write('\rCarregado!     ')

boot_logo = """
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   .     ,,,,,   *@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@(  .       .,       .., @@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@         ,,***,,,,,,,,,,,,@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@ .    ,  @@@@@@@*,,,,,,,,,,, @@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@  %, ,% @@@@@@@@@@,,,,*,,,,,  @@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@      , @@@@@@@@@@@@**,,*,,,,  @@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@    . ,  @@@@@@@@@@@**,,*,,,,  @@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@   , ,  @@@@@@@@@@@**,,*,,,,  @@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@ .       @@@@@@@@@***,*,,,,  @@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@ . . , , @@@@@@@@**,**,,,  @@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@ ..  ,   @@@@@@*****,,,  @@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@...      @@@***/*,,,  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@         ****//,,, @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ .        *//*,. @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,@         ***. @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,@@@ .        .@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  .   (%  .@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ ///   %  % %@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ *////    .%%% %@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  /////  % %  *  %@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ *//////   %(.%    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  *////// .    / %%/ @@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ *///////     ..     @@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  */////     #%%     @@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,      %   %.%     @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,   %.#%#.  ..@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
"""

boot_text = """
  /$$$$$$   /$$$$$$  /$$$$$$$   /$$$$$$                                  
 /$$__  $$ /$$__  $$| $$__  $$ /$$__  $$                                 
| $$  \__/| $$  \ $$| $$  \ $$| $$  \ $$                                 
| $$      | $$  | $$| $$$$$$$/| $$$$$$$$                                 
| $$      | $$  | $$| $$____/ | $$__  $$                                 
| $$    $$| $$  | $$| $$      | $$  | $$                                 
|  $$$$$$/|  $$$$$$/| $$      | $$  | $$                                 
 \______/  \______/ |__/      |__/  |__/                                 
                                                                         
                                                                         
                                                                         
 /$$      /$$  /$$$$$$  /$$   /$$  /$$$$$$   /$$$$$$  /$$$$$$$$ /$$$$$$$ 
| $$$    /$$$ /$$__  $$| $$$ | $$ /$$__  $$ /$$__  $$| $$_____/| $$__  $$
| $$$$  /$$$$| $$  \ $$| $$$$| $$| $$  \ $$| $$  \__/| $$      | $$  \ $$
| $$ $$/$$ $$| $$$$$$$$| $$ $$ $$| $$$$$$$$| $$ /$$$$| $$$$$   | $$$$$$$/
| $$  $$$| $$| $$__  $$| $$  $$$$| $$__  $$| $$|_  $$| $$__/   | $$__  $$
| $$\  $ | $$| $$  | $$| $$\  $$$| $$  | $$| $$  \ $$| $$      | $$  \ $$
| $$ \/  | $$| $$  | $$| $$ \  $$| $$  | $$|  $$$$$$/| $$$$$$$$| $$  | $$
|__/     |__/|__/  |__/|__/  \__/|__/  |__/ \______/ |________/|__/  |__/
"""
print(boot_logo) #dá print na logo da copa
time.sleep(1) #tempo para visualização
#loading()
import filecheck #importa o arquivo de checagem dos arquivos
done = "true"

#fake loading#
###################################################################
#for x in range (0,5):
#  texto_load = "Carregando o Copa Manager" + "." * x
#  print (texto_load, end="\r")
#  time.sleep(0.5)
###################################################################

time.sleep(1) #tempo para visualização
print(boot_text) #dá print na logo do CopaManager
time.sleep(0.5) #tempo para visualização
print("Produzido por Kaian Vinicius, @Kaian32")
time.sleep(3) #tempo para visualização