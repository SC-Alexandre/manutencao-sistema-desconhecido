usuarios = []

def cadastrar_usuario(nome, idade):
    nome = nome.strip()
    
    if not nome:
        print("Erro: o nome não pode ser vazio.")
        return False
    
    if not isinstance(idade, int) or isinstance(idade, bool) or idade <= 0:
        print("Erro: a idade deve ser um número inteiro positivo.")
        return False
              
    usuarios.append({
        "nome": nome,
        "idade": idade
    })
    
    print("Usuário cadastrado com sucesso!")
    return True

def listar():
    for i in range(len(usuarios)):
        print("Usuário:", usuarios[i])

def buscar(nome):
    for u in usuarios:
        if u == nome:
            return True
    return False