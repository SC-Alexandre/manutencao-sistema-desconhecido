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

def listar_usuarios():
    if not usuarios:
        print("Nenhum usuário cadastrado.")
        return

    for usuario in usuarios:
        print(f"Nome: {usuario['nome']} | Idade: {usuario['idade']}")

def buscar_usuarios(nome):
    nome = nome.strip()

    for usuario in usuarios:
        if usuario["nome"].casefold() == nome.casefold():
            return usuario
    return None