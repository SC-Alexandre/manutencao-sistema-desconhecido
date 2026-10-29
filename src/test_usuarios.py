
import unittest
from usuarios import (
    usuarios,
    cadastrar_usuario,
    buscar_usuarios
)

class TestUsuarios(unittest.TestCase):

    def setUp(self):
        usuarios.clear()

    def test_cadastro_valido(self):
        resultado = cadastrar_usuario("Alexandre", 25)

        self.assertTrue(resultado)
        self.assertEqual(len(usuarios), 1)
        self.assertEqual(usuarios[0]["nome"], "Alexandre")
        self.assertEqual(usuarios[0]["idade"], 25)

    def test_cadastro_nome_vazio(self):
        resultado = cadastrar_usuario("", 25)

        self.assertFalse(resultado)
        self.assertEqual(len(usuarios), 0)

    def test_cadastro_idade_invalida(self):
        resultado = cadastrar_usuario("Maria", 0)

        self.assertFalse(resultado)
        self.assertEqual(len(usuarios), 0)

    def test_cadastro_idade_texto(self):
        resultado = cadastrar_usuario("João", "20")

        self.assertFalse(resultado)
        self.assertEqual(len(usuarios), 0)

    def test_busca_usuario_existente(self):
        cadastrar_usuario("Maria", 30)

        resultado = buscar_usuarios("Maria")

        self.assertIsNotNone(resultado)
        self.assertEqual(resultado["nome"], "Maria")
        self.assertEqual(resultado["idade"], 30)

    def test_busca_usuario_inexistente(self):
        resultado = buscar_usuarios("Carlos")

        self.assertIsNone(resultado)

    def test_busca_sem_diferenciar_maiusculas(self):
        cadastrar_usuario("Alexandre", 25)

        resultado = buscar_usuarios("alexandre")

        self.assertIsNotNone(resultado)
        self.assertEqual(resultado["nome"], "Alexandre")

if __name__ == "__main__":
    unittest.main()
