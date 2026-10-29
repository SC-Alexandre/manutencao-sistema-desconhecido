usuarios = []

def cadastrar(nome, idade):
    if nome != "" and idade > 0:
        usuarios.append(nome)

def listar():
    for i in range(len(usuarios)):
        print("Usuário:", usuarios[i])

def buscar(nome):
    for u in usuarios:
        if u == nome:
            return True
    return False