# Documentação do Sistema de Cadastro de Usuários

## 1. O que o sistema faz

O sistema permite cadastrar, listar e buscar usuários por nome. Para cada usuário, são armazenados o nome e a idade.

O sistema valida os dados informados e permite consultar se um usuário está cadastrado.

Os dados são armazenados em uma lista na memória durante a execução do programa.

## 2. Como usar as funções

### `cadastrar_usuario(nome, idade)`

Realiza o cadastro de um usuário após validar as informações.

**Exemplo:**
```python
cadastrar_usuario("Alexandre", 25)
```

**Comportamento:**
- Retorna `True` se o cadastro for realizado.
- Retorna `False` se os dados forem inválidos.
- Armazena o nome e a idade do usuário.

### `listar_usuarios()`

Exibe todos os usuários cadastrados, mostrando nome e idade.

**Exemplo:**
```python
listar_usuarios()
```

Se não houver usuários cadastrados, o sistema informa que a lista está vazia.

### `buscar_usuario(nome)`

Busca um usuário pelo nome.

**Exemplo:**
```python
resultado = buscar_usuario("Alexandre")
print(resultado)
```

**Comportamento:**
- Retorna um dicionário contendo o nome e a idade se encontrar o usuário.
- Retorna `None` se o usuário não existir.
- A busca não diferencia letras maiúsculas e minúsculas.

## 3. Melhorias realizadas

As seguintes melhorias foram implementadas no código original:

1. **Refatoração:** os nomes das funções foram alterados para torná-las mais claros e descritivos.
2. **Armazenamento de dados:** o sistema passou a armazenar nome e idade utilizando dicionários.
3. **Validação de dados:** foram adicionadas verificações para impedir nomes vazios, idades inválidas e valores que não sejam números inteiros positivos.
4. **Melhoria na busca:** a função retorna os dados do usuário encontrado ou `None` quando não há resultados.
5. **Melhoria na listagem:** a função percorre diretamente a lista de usuários, tornando o código mais simples e legível.
6. **Tratamento de situações sem dados:** o sistema informa quando não existem usuários cadastrados para listar.

## 4. Conclusão

O sistema foi refatorado para melhorar sua organização, legibilidade e confiabilidade. As correções e validações contribuem para reduzir erros durante o cadastro e a busca de usuários, facilitando futuras manutenções.