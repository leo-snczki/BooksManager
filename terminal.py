from readkeys import getch
import os
import sys                                               

# _______  _______  ______   ______   _____  ______           _       
#(_______)(_______)(_____ \ |  ___ \ (_____)|  ___ \    /\   | |      
# _        _____    _____) )| | _ | |   _   | |   | |  /  \  | |      
#| |      |  ___)  (_____ ( | || || |  | |  | |   | | / /\ \ | |      
#| |_____ | |_____       | || || || | _| |_ | |   | || |__| || |_____ 
# \______)|_______)      |_||_||_||_|(_____)|_|   |_||______||_______)                                                                   


if sys.platform in ('linux', 'darwin'):
    CLEAR = 'clear'
elif sys.platform == 'win32':
    CLEAR = 'cls'
else:
    print('Platform not supported', file=sys.stderr)
    exit(1)

# ============================
# _limpar_term
# ============================
def limpar_term() -> None:
    os.system(CLEAR)

# ============================
# _click_para_continuar
# ============================
def click_para_continuar() -> None:
    print("\n Pressione para continuar...")
    getch()