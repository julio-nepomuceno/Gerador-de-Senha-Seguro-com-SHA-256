import random
import os
import string
import getpass
from termcolor import colored
import hashlib

def gerar_senha():
    os.system('cls' if os.name == 'nt' else 'clear')
    caracteres = (
            random.choices(string.ascii_lowercase, k=2) +  
            random.choices(string.ascii_uppercase, k=2) +  
            random.choices(string.digits, k=2) +  
            random.choices("!@#$%^&*()", k=2)  
        )
    random.shuffle(caracteres)
    user_senha = ''.join(caracteres)
    try:
        username = os.getlogin()
    except:
        username = getpass.getuser()
    username_completo = username  + ''.join(random.choices("!@#$%^&*", k=5))
    print(colored(f"USUÁRIO ➤  {username_completo}", "light_blue"))
    print(colored(f"SENHA ➤  {user_senha}", "light_green"))
    crip_senha(user_senha)

def crip_senha(senha):
    senha_crip = hashlib.sha256(senha.encode()).hexdigest()
    print(colored(f"SENHA CRIPTOGRAFADA ➤  {senha_crip}", "light_cyan"))
gerar_senha()