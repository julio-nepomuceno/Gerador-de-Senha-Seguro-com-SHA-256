# 🔐 Gerador de Usuário e Senha Segura com Criptografia SHA-256  

Este é um **gerador de usuário e senha aleatória**, que cria um nome de usuário personalizado e uma senha forte contendo letras, números e símbolos. Além disso, a senha gerada é **criptografada com SHA-256**, garantindo maior segurança.  

## 🚀 Tecnologias Utilizadas  
- **Python** 🐍  
- **Bibliotecas:** `random`, `os`, `string`, `getpass`, `hashlib`, `termcolor`  

## 📌 Funcionalidades  
✅ Gera um nome de usuário aleatório baseado no usuário do sistema.  
✅ Cria uma senha segura com caracteres variados.  
✅ Exibe o usuário e a senha gerados no terminal com cores.  
✅ Criptografa a senha gerada usando **SHA-256**.  
✅ Suporte para Windows, Linux e macOS.  

## 📷 Exemplo de Execução  

```sh
========================================
 USUÁRIO ➤  MeuUsuario!@#%  
 SENHA ➤  Gv2f#9!  
 SENHA CRIPTOGRAFADA ➤  d7a5f1c... (hash SHA-256)
========================================
